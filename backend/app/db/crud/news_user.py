from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class NewsuserCrud:

    @staticmethod
    async def get_by_login_id(login_id:str,db:AsyncSession):
        pass

    @staticmethod
    async def create(login_id:str,db:AsyncSession):
        pass