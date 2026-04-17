from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class NewsuserService:

    @staticmethod
    async def my_newsuser(login_id:str,limit:int, db:AsyncSession):
        pass

    @staticmethod
    async def add_newsuser(login_id:str,db:AsyncSession):
        pass