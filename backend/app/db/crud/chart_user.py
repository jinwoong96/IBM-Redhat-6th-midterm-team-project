from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.scheme.chart_user import ChartuserUpdate

class ChartuserCrud:

    @staticmethod
    async def get_by_id_code(user_id:str, item_code:str, limit:int, db:AsyncSession):
        pass

    @staticmethod
    async def create_all(user_id:str,chart:ChartuserUpdate,db:AsyncSession):
        pass