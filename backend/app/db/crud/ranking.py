from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.ranking import Ranking
from sqlalchemy.orm import joinedload

class RankingCrud:

    @staticmethod
    async def get_by_login_id(login_id:str, db: AsyncSession):
        result = await db. execute(
            select(Ranking)
            .options(joinedload(Ranking.user))
            .filter(Ranking.login_id==login_id)
        )
        return result.scalars().first()


    @staticmethod
    async def get_top10_rank(db:AsyncSession):
        result = await db. execute(
            select(Ranking)
            .options(joinedload(Ranking.user))
                .order_by(Ranking.max_accounts.desc())
                .limit(10)
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_all_count(db: AsyncSession):
        result = await db.execute(select(Ranking))
        all_re = result.scalars().all()
        return len(all_re)

    # @staticmethod
    # async def update(db: AsyncSession, ranking: Ranking):
    #     await db.commit()
    #     await db.refresh(ranking)
    #     return ranking
#업데이트 고민중

    @staticmethod
    async def create(login_id: str, max_accounts:int, max_plus:float, day:int, db:AsyncSession):
        new_ranking = Ranking(login_id=login_id, max_accounts=max_accounts, max_plus=max_plus, day=day)
        db.add(new_ranking)