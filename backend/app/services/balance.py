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

        if trade_data.buy_type == "buy":
            if balance:
                # 1. 기존 잔고 매수 계산
                new_quantity = balance.quantity + trade_data.quantity
                new_purchase_price = balance.purchase_price + total_trade_price
                new_val_price = new_quantity * trade_data.price
                new_val_profit_and_loss = new_val_price - new_purchase_price
                new_rate_of_return = round((new_val_profit_and_loss / new_purchase_price) * 100.0, 2) if new_purchase_price > 0 else 0.0

                update_data = {
                    "quantity": new_quantity,
                    "purchase_price": new_purchase_price,
                    "val_price": new_val_price,
                    "val_profit_and_loss": new_val_profit_and_loss,
                    "rate_of_return": new_rate_of_return
                }
                # 단일 업데이트 CRUD 호출 (내부에서 flush)
                await BalanceCrud.update(balance, update_data, db)

            else:
                # 2. 신규 잔고 매수 계산
                new_balance_data = {
                    "login_id": login_id,
                    "item_code": trade_data.item_code,
                    "quantity": trade_data.quantity,
                    "purchase_price": total_trade_price,
                    "val_price": trade_data.quantity * trade_data.price,
                    "val_profit_and_loss": 0, 
                    "rate_of_return": 0.0
                }
                # 신규 생성 CRUD 호출 (내부에서 flush)
                await BalanceCrud.create(new_balance_data, db)

        elif trade_data.buy_type == "sell":
            if not balance or balance.quantity < trade_data.quantity:
                raise HTTPException(status_code=400, detail="보유 수량이 부족하여 매도할 수 없습니다.")
            
            new_quantity = balance.quantity - trade_data.quantity
            
            if new_quantity == 0:
                # 3. 전량 매도 (삭제 CRUD 호출, 내부에서 flush)
                await BalanceCrud.delete(balance, db)
            else:
                # 4. 부분 매도 계산
                avg_price = balance.purchase_price / balance.quantity
                cost_deduction = int(avg_price * trade_data.quantity)
                new_purchase_price = balance.purchase_price - cost_deduction
                
                new_val_price = new_quantity * trade_data.price
                new_val_profit_and_loss = new_val_price - new_purchase_price
                new_rate_of_return = round((new_val_profit_and_loss / new_purchase_price) * 100.0, 2) if new_purchase_price > 0 else 0.0

                update_data = {
                    "quantity": new_quantity,
                    "purchase_price": new_purchase_price,
                    "val_price": new_val_price,
                    "val_profit_and_loss": new_val_profit_and_loss,
                    "rate_of_return": new_rate_of_return
                }
                # 단일 업데이트 CRUD 호출 (내부에서 flush)
                await BalanceCrud.update(balance, update_data, db)

        return total_trade_price