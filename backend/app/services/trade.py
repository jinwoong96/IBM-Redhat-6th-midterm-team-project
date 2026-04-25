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
        #  의미 없는 수량/금액 0 거래 차단
        if trade_data.quantity <= 0 or trade_data.price <= 0:
            raise HTTPException(status_code=400, detail="거래 수량 및 가격은 1 이상이어야 합니다.")

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
            
            # [1] 이번 거래의 총액 계산
            total_trade_price = trade_data.price * trade_data.quantity

            # [2] 매수/매도 분기 로직: 수량, 총원금, 유저 현금 갱신
            if trade_data.buy_type == "buy":
                if user.money < total_trade_price:
                    raise HTTPException(status_code=400, detail="현금 잔액이 부족하여 매수할 수 없습니다.")   
                
                user.money -= total_trade_price 
                
                if balance:
                    balance.quantity += trade_data.quantity
                    balance.purchase_price += total_trade_price
                else:
                    balance = Balance(
                        login_id=login_id,
                        item_code=trade_data.item_code,
                        quantity=trade_data.quantity,
                        purchase_price=total_trade_price,
                        val_price=0, 
                        val_profit_and_loss=0, 
                        rate_of_return=0.0
                    )
                    db.add(balance)
                    
            elif trade_data.buy_type == "sell":
                if not balance or balance.quantity < trade_data.quantity:
                    raise HTTPException(status_code=400, detail="보유 수량이 부족하여 매도할 수 없습니다.")                
                
                user.money += total_trade_price 
                
                # 내부 계산용 매입 단가 (DB에 컬럼 없음)
                avg_price = balance.purchase_price / balance.quantity
                cost_deduction = int(avg_price * trade_data.quantity)
                
                balance.quantity -= trade_data.quantity
                balance.purchase_price -= cost_deduction
                
                if balance.quantity == 0:
                    await db.delete(balance)
                    balance = None 
            
            await db.flush()
            
            # [3] 변경된 종목의 평가금액(val_price) 및 수익률 갱신
            if balance:
                # 체결 가격이 해당 시점의 현재가이므로 평가금액 갱신에 사용
                balance.val_price = balance.quantity * trade_data.price
                balance.val_profit_and_loss = balance.val_price - balance.purchase_price
                
                if balance.purchase_price > 0:
                    balance.rate_of_return = round((balance.val_profit_and_loss / balance.purchase_price) * 100.0, 2)
                else:
                    balance.rate_of_return = 0.0

            await db.flush()

            # [4] 유저 전체 보유 자산 평가금액(valuation) 갱신
            all_balances_result = await db.execute(select(Balance).filter_by(login_id=login_id))
            all_balances = all_balances_result.scalars().all()
            
            user.valuation = sum(b.val_price for b in all_balances)
            
            # [5] 거래 내역 생성
            new_trade = await TradeCrud.create(login_id, trade_data, db)
            
            await db.commit()
            await db.refresh(new_trade)
            
            return new_trade

        except HTTPException:
            await db.rollback()
            raise
        
        except Exception:
            await db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail="거래를 처리하는 중 서버 내부에 예상치 못한 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
            )