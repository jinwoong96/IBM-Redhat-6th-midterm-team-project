from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.ranking import Ranking
from app.db.scheme.ranking import RankingUpdate


class RankingCrud:

    @staticmethod
    async def update_ranking(rank:RankingUpdate,user_id:int,
                   db: AsyncSession):
        # 1. user_id로 행 조회
        # 2. 있다면 지금 입력되는 최대 잔고 보다 원래 입력되있는 최대잔고보다 크면 업데이트
        # 3. 없다면 새로운 행에 입력한 데이트를 추가하여 db.add
        # 새로운 랭킹을 반환
        pass

    @staticmethod
    async def get_top10_rank(db:AsyncSession):
        # 최대 잔고 내림차순 정렬 후
        # 10개 리스트 리턴
        pass