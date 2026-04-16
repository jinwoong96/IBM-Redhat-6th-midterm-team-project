from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.trade import Trade
from app.db.scheme.trade import TradeCreate

class TradeCrud:

    @staticmethod
    async def get_by_login_id(login_id:str,limit:int,offset:int,db:AsyncSession):
        pass

    @staticmethod
    async def create(login_id:str,trade:TradeCreate,db:AsyncSession):
        pass