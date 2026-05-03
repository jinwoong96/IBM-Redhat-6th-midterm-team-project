from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.balance import BalanceCrud
from app.db.models.balance import Balance
from app.db.scheme.trade import TradeCreate
class BalanceService:
    @staticmethod
    async def my_balance(login_id: str, db: AsyncSession):
        try:
            # 잔고 내역 조회 (잔고가 없으면 빈 리스트 [] 반환)
            balances = await BalanceCrud.get_by_id(login_id, db)
            return balances
            
        except Exception:
            # 의도치 않은 파이썬/DB 내부 에러 방어
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="잔고 내역을 불러오는 중 서버에 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
            )
        
    @staticmethod
    async def process_trade_balance(login_id: str, trade_data: TradeCreate, db: AsyncSession):
        balance = await BalanceCrud.get_balance_by_user_and_item(login_id, trade_data.item_code, db)
        total_trade_price = trade_data.price * trade_data.quantity

        # 1. 매수/매도 분기 로직: 수량 및 원금 갱신
        if trade_data.buy_type == "buy":
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
            
            avg_price = balance.purchase_price / balance.quantity
            cost_deduction = int(avg_price * trade_data.quantity)
            
            balance.quantity -= trade_data.quantity
            balance.purchase_price -= cost_deduction
            
            if balance.quantity == 0:
                await BalanceCrud.delete(balance, db)
                balance = None 

        await db.flush()

        # 2. 평가금액 및 수익률 갱신
        if balance:
            balance.val_price = balance.quantity * trade_data.price
            balance.val_profit_and_loss = balance.val_price - balance.purchase_price
            
            if balance.purchase_price > 0:
                balance.rate_of_return = round((balance.val_profit_and_loss / balance.purchase_price) * 100.0, 2)
            else:
                balance.rate_of_return = 0.0

        await db.flush()
        return total_trade_price
