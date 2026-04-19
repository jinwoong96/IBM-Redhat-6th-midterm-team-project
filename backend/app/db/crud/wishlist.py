from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.wishlist import Wishlist  

class WishlistCrud:

    @staticmethod
    async def create(login_id: str, item_code: str, db: AsyncSession):
        db_wish = Wishlist(login_id=login_id, item_code=item_code)
        db.add(db_wish)
        await db.flush() 
        return db_wish

    @staticmethod
    async def get_all_by_login_id(login_id: str, db: AsyncSession):
      
        result = await db.execute(select(Wishlist).filter(Wishlist.login_id == login_id))
        return result.scalars().all()

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