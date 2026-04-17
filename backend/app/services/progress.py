from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.db.scheme.user import UserUpdate
from sqlalchemy.future import select
from app.db.crud.user import UserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class ProgressService:

    @staticmethod
    async def next(login_id:str,db:AsyncSession):
        # 필요하면 crud는 이름 규칙 맞춰서 새로 만들어야함
        pass