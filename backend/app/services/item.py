from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.item import Item
from sqlalchemy.future import select
from app.db.crud.item import ItemCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class ItemService:

    @staticmethod
    async def all_item(user_id:str,db:AsyncSession):
        # user_id로 로그인되있는 유저 검증(에러처리)
        # ItemCrud.get_all_item(db)로 모든 종목을 반환
        pass


    @staticmethod
    async def top_10_item(user_id:str,db:AsyncSession):
        # user_id로 로그인되있는 유저 검증(에러처리)
        # ItemCrud.get_top_10_item(db)로 10 종목 반환
        pass