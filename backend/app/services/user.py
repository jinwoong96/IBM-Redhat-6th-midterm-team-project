from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.db.scheme.user import UserCreate, UserLogin, UserUpdate
from sqlalchemy.future import select
from app.db.crud.user import UserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token



class UserService:

    @staticmethod
    async def signup(user: UserCreate, db: AsyncSession):
        pass

    @staticmethod
    async def login(user:UserLogin,db:AsyncSession):
        pass

    @staticmethod
    async def get_user(login_id:str,db:AsyncSession):
        pass

    @staticmethod
    async def update_user(login_id:str,userupdate:UserUpdate,db:AsyncSession):
        pass
