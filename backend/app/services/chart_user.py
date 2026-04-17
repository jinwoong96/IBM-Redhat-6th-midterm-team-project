from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.chart_user import ChartUser
from sqlalchemy.future import select
from app.db.crud.chart_user import ChartuserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
class ChartuserService:

    @staticmethod
    async def get_chartuser(login_id:str, item_code:str, limit:int, db:AsyncSession):
        pass

    @staticmethod
    async def init_chartuser(login_id:str,db:AsyncSession):
        pass

    @staticmethod
    async def get_itemlist(login_id:str, db:AsyncSession):
        pass