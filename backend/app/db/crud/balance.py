from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.balance import Balance

class BalanceCrud:
    @staticmethod
    async def get_by_id(login_id: str, db: AsyncSession):
        result = await db.execute(
            select(Balance).filter(Balance.login_id == login_id)
        )
        return result.scalars().all()