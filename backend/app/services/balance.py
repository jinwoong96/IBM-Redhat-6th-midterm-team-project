from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud.balance import BalanceCrud

class BalanceService:
    @staticmethod
    async def my_balance(login_id: str, db: AsyncSession):
        return await BalanceCrud.get_by_id(login_id, db)