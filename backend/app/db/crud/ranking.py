from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.ranking import Ranking
from app.db.scheme.ranking import RankingUpdate


class RankingCrud:

    @staticmethod
    async def get_by_login_id(login_id:str,
                   db: AsyncSession):
        pass

    @staticmethod
    async def get_top10_rank(db:AsyncSession):
        pass