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
            user = await db.get(User, login_id)
            if not user:
                raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
            result = await db.execute(
                select(Balance).filter_by(login_id=login_id, item_code=trade_data.item_code)
            )
            balance = result.scalars().first()
            # 이번 거래의 총액 ; 가격 * 수량 => 계산 편의를 위해 영수증 총액 미리 끊어놓음
            total_trade_price = trade_data.price * trade_data.quantity

            if trade_data.buy_type == "buy":
                if user.money < total_trade_price:
                    raise HTTPException(status_code=400, detail="현금 잔액이 부족합니다.")   
                user.money -= total_trade_price 
                # 기존 보유 종목이면, 기존 수량에 새로 산 수량을 더하고, 기존 '총 매입원금'에 새로 쓴 돈을 더함
                if balance:
                    balance.quantity += trade_data.quantity
                    balance.purchase_price += total_trade_price
                else:
                    # 신규 매수 종목이면 Balance 레코드 생성
                    # 평가금액과 수익률 관련 초기값은 모두 0으로 
                    balance = Balance(
                        login_id=login_id,
                        item_code=trade_data.item_code,
                        quantity=trade_data.quantity,
                        purchase_price=total_trade_price,
                        val_price=0, val_profit_and_loss=0, rate_of_return=0.0
                    )
                    db.add(balance)
            elif trade_data.buy_type == "sell":
                if not balance or balance.quantity < trade_data.quantity:
                    raise HTTPException(status_code=400, detail="보유 수량이 부족하여 매도할 수 없습니다.")                
                user.money += total_trade_price #  유저 현금 증가
                # 기존 평단가에 맞춰 매도한 만큼 원금(purchase_price) 비율 차감
                # (총원금 / 수량)으로 1주당 평균 단가 -> 매도 수량만큼 곱하여 '차감할 원금'계산
                avg_price = balance.purchase_price / balance.quantity
                cost_deduction = int(avg_price * trade_data.quantity)
                balance.quantity -= trade_data.quantity
                balance.purchase_price -= cost_deduction
                #  수량이 0이 되면 DB에서 해당 잔고 레코드를 삭제 (잔고 조회시 안 보이게 됨)
                if balance.quantity == 0:
                    await db.delete(balance)
                    balance = None 
            await db.flush() # 변경된 잔고(및 삭제 상태)를 DB 세션에 임시 반영
           
            #  잔고 업데이트 
            if balance:
                balance.val_price = balance.quantity * trade_data.price
                balance.val_profit_and_loss = balance.val_price - balance.purchase_price
                if balance.purchase_price > 0:
                    balance.rate_of_return = round((balance.val_profit_and_loss / balance.purchase_price) * 100.0, 2)

            await db.flush()

            all_balances_result = await db.execute(select(Balance).filter_by(login_id=login_id))
            all_balances = all_balances_result.scalars().all()
            user.valuation = sum(b.val_price for b in all_balances)
            new_trade = await TradeCrud.create(login_id, trade_data, db)
            await db.commit()
            await db.refresh(new_trade)
            return new_trade

        except HTTPException:
            await db.rollback()
            raise
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=400, detail=str(e))