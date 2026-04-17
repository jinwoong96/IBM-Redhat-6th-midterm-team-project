from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.trade import Trade
from sqlalchemy.future import select
from app.db.crud.wishlist import WishlistCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token

class WishlistService:

    @staticmethod
    async def add_wishlist(login_id:str,item_code:str,db:AsyncSession):
        pass

    @staticmethod
    async def user_wishlist(login_id:str,db:AsyncSession):
        pass
    
    @staticmethod
    async def delete_wishlist(login_id:str,item_code:str,db:AsyncSession):
        pass