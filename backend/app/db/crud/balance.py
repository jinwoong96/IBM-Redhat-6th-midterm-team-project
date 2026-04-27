from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from app.db.models.balance import Balance
from app.db.models.chart_user import ChartUser
from app.db.models.item import Item
class BalanceCrud:
    @staticmethod
    async def get_by_id(login_id: str, db: AsyncSession):
     
        stmt = (
            select(
                Balance.item_code, 
                Item.item_name, 
                Balance.quantity,
                Balance.purchase_price,
                Balance.val_price,
                Balance.val_profit_and_loss,
                Balance.rate_of_return
            )
            .join(Item, Balance.item_code == Item.item_code)
            .where(Balance.login_id == login_id)
        )
        
        result = await db.execute(stmt)
        return result.mappings().all()
    

    @staticmethod
    async def get_balance_with_prices(login_id: str, next_day: int,db: AsyncSession):
        result = await db.execute(
            select(Balance, ChartUser.end_price, Item.item_name)
            .join(ChartUser, onclause=and_(
                Balance.item_code == ChartUser.item_code,
                ChartUser.login_id == login_id,
                ChartUser.day == next_day
            ))
            .join(Item, onclause=Balance.item_code == Item.item_code)
            .filter(Balance.login_id == login_id)
        )
        return result.all()