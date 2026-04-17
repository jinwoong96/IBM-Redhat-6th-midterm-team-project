from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.user import User
from app.db.scheme.user import UserCreate, UserUpdate



class UserCrud:
    
    @staticmethod
    async def create(user:UserCreate,db:AsyncSession):
        pass


    @staticmethod
    async def get_by_login_id(login_id:str,db:AsyncSession):
        pass

    @staticmethod
    async def update_refresh_token_by_id(login_id:str,
        refresh_token:str,
        db:AsyncSession):
        pass


    @staticmethod
    async def update_by_id(login_id:str,userupdate:UserUpdate,db:AsyncSession):
        pass
