from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.ranking import Ranking
from app.db.scheme.ranking import RankingUpdate



class ProgressCrud:


    @staticmethod
    async def get_by_id_balance(user_id:int,db:AsyncSession):
        # user_id에 해당되는 잔고를 리스트로 뽑음
        # 리스트 중 종목 코드만 리스트로 뽑음
        pass

    @staticmethod
    async def get_by_id_chart(user_id:int,item_code:list,db:AsyncSession):
        # user_id와 모든 item_code를 조회해서 해당되는 chart_user를 뽑음
        # 
        pass

    @staticmethod
    async def next_update(end_price:int,db:AsyncSession):
        #
        pass