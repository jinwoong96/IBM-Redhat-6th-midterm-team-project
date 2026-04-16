from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.wishlist import Wishlist


class WishlistCrud:

    @staticmethod
    async def create(login_id:str, item_code:str,db:AsyncSession):
        pass

    @staticmethod
    async def get_by_login_id(login_id:str,db:AsyncSession):
        pass

    @staticmethod
    async def delete_by_id_itemcode(login_id:str,item_code:str,db:AsyncSession):
        pass