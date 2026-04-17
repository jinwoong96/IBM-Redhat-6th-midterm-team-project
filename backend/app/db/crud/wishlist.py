from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.wishlist import WishList


class WishlistCrud:

    @staticmethod
    async def create(login_id:str, item_code:str,db:AsyncSession):
        db_wish=WishList(login_id=login_id, item_code=item_code)
        db.add(db_wish)
        await db.flush()
        return db_wish
    @staticmethod
    async def get_by_login_id(login_id:str,db:AsyncSession):
        result=await db.execute(select(WishList).filter(WishList.login_id == login_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def delete_by_id_itemcode(login_id:str,item_code:str,db:AsyncSession):
        result=await db.get(login_id, item_code)
        if result:
            await db.delete(result)
            await db.flush()
            return result
        return None