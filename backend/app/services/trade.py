from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status

from app.db.models.trade import Trade
from app.db.models.user import User
from app.db.models.balance import Balance
from app.db.crud.trade import TradeCrud
from app.db.scheme.trade import TradeCreate

class TradeService:

    @staticmethod
    async def my_trade_list(login_id: str, limit: int, offset: int, db: AsyncSession):        
        return await TradeCrud.get_list_by_login_id(login_id, limit, offset, db)

    @staticmethod
    async def new_trade(login_id: str, trade_data: TradeCreate, db: AsyncSession):
        if trade_data.buy_type not in ("buy", "sell"):
            raise HTTPException(status_code=400, detail="buy_type은 'buy' 또는 'sell' 이어야 합니다.")

        try:
            # 1. 현재 거래하려는 유저 확인
            user = await db.get(User, login_id)
            if not user:
                raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

            # 2. 거래하려는 종목의 현재 잔고 조회
            result = await db.execute(
                select(Balance).filter_by(login_id=login_id, item_code=trade_data.item_code)
            )
            balance = result.scalars().first()

            total_trade_price = trade_data.price * trade_data.quantity

            # ========================================================
            # [A] 매수 (Buy)
            # ========================================================
            if trade_data.buy_type == "buy":
                if user.money < total_trade_price:
                    raise HTTPException(status_code=400, detail="현금 잔액이 부족합니다.")
                
                user.money -= total_trade_price # 💸 유저 현금 차감

                if balance:
                    # 기존 보유 종목이면 수량과 총 매입금액 증가
                    balance.quantity += trade_data.quantity
                    balance.purchase_price += total_trade_price
                else:
                    # 신규 매수 종목이면 Balance 레코드 생성
                    balance = Balance(
                        login_id=login_id,
                        item_code=trade_data.item_code,
                        quantity=trade_data.quantity,
                        purchase_price=total_trade_price,
                        val_price=0, val_profit_and_loss=0, rate_of_return=0.0
                    )
                    db.add(balance)

            # ========================================================
            # [B] 매도 (Sell)
            # ========================================================
            elif trade_data.buy_type == "sell":
                if not balance or balance.quantity < trade_data.quantity:
                    raise HTTPException(status_code=400, detail="보유 수량이 부족하여 매도할 수 없습니다.")
                
                user.money += total_trade_price # 💵 유저 현금 증가

                # 기존 평단가에 맞춰 매도한 만큼 원금(purchase_price) 비율 차감
                avg_price = balance.purchase_price / balance.quantity
                cost_deduction = int(avg_price * trade_data.quantity)

                balance.quantity -= trade_data.quantity
                balance.purchase_price -= cost_deduction

                # 💡 핵심: 수량이 0이 되면 DB에서 해당 잔고 레코드를 삭제 (잔고 조회시 안 보이게 됨)
                if balance.quantity == 0:
                    await db.delete(balance)
                    balance = None 

            await db.flush() # 변경된 잔고(및 삭제 상태)를 DB 세션에 임시 반영

            # ========================================================
            # [C] 잔고 평가액 및 유저 총 평가금액 갱신
            # ========================================================
            # 1. 잔고 업데이트 (당일 매매 가격 = 현재가 로 간주)
            if balance:
                balance.val_price = balance.quantity * trade_data.price
                balance.val_profit_and_loss = balance.val_price - balance.purchase_price
                if balance.purchase_price > 0:
                    balance.rate_of_return = round((balance.val_profit_and_loss / balance.purchase_price) * 100.0, 2)

            await db.flush()

            # 2. 유저 테이블 업데이트 (valuation = 보유 주식의 총 가치)
            all_balances_result = await db.execute(select(Balance).filter_by(login_id=login_id))
            all_balances = all_balances_result.scalars().all()
            user.valuation = sum(b.val_price for b in all_balances)

            # ========================================================
            # [D] 체결(Trade) 내역 기록 (TradeCrud 사용)
            # ========================================================
            new_trade = await TradeCrud.create(login_id, trade_data, db)

            # 모든 작업이 성공했으므로 커밋
            await db.commit()
            await db.refresh(new_trade)
            return new_trade

        except HTTPException:
            await db.rollback()
            raise
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=400, detail=str(e))