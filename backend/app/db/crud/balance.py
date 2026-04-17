from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.balance import Balance
from app.db.scheme.balance import BalanceUpdate


class BalanceCrud:
    @staticmethod
    async def get_by_id(login_id:str,db:AsyncSession):
        pass
