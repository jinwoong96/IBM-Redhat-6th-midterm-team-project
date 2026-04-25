from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.balance import Balance
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