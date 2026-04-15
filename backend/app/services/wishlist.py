from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.trade import Trade
from sqlalchemy.future import select
from app.db.crud.wishlist import WishlistCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token

class WishlistService:

    @staticmethod
    async def add_wishlist(item_code:str,user_id:str,db:AsyncSession):
        # user_id 가 user테이블에 있는지 확인
        # WishlistCrud.new_wishlist 로 새 위시리스트 만들어서 반환
        pass

    @staticmethod
    async def user_wishlist(user_id:int,current_user_id:str,db:AsyncSession):
        # current_user_id 가 user테이블에 있는지 확인
        # WishlistCrud.get_by_id 로 아이디에 해당되는 위시리스트 전부 리스트로 반환
        pass
    
    @staticmethod
    async def delete_wishlist(item_code:str,user_id:str,db:AsyncSession):
        # user_id 있는지 확인(예외처리)
        # WishlistCrud.delete_by_id_itemcode 로 행삭제
        pass