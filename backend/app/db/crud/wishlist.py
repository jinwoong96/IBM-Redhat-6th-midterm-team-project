from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.wishlist import Wishlist  
from app.db.models import Item,ChartUser
class WishlistCrud:

    @staticmethod
    async def create(login_id: str, item_code: str, db: AsyncSession):
        db_wish = Wishlist(login_id=login_id, item_code=item_code)
        db.add(db_wish)
        await db.flush() 
        return db_wish

    @staticmethod
    async def get_all_by_login_id(login_id: str, db: AsyncSession):
        stmt = (
            select(
                Wishlist.item_code,
                Item.item_name,
                Item.category_name,
                ChartUser.flu_range_percent,
                ChartUser.end_price
            )
            .join(Item, Wishlist.item_code == Item.item_code)
            .join(ChartUser, (Wishlist.item_code == ChartUser.item_code) & (Wishlist.login_id == ChartUser.login_id))
            .where(Wishlist.login_id == login_id)
        )
        result = await db.execute(stmt)
        return result.mappings().all()
            
    @staticmethod
    async def get_by_user_and_item(login_id: str, item_code: str, db: AsyncSession):
        
        result = await db.execute(
            select(Wishlist).filter(Wishlist.login_id == login_id, Wishlist.item_code == item_code)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def delete(db_wish: Wishlist, db: AsyncSession):
       
        await db.delete(db_wish)
        await db.flush()