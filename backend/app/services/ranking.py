from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.ranking import Ranking
from app.db.scheme.ranking import RankingUpdate
from sqlalchemy.future import select
from app.db.crud.ranking import RankingCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class RankingService:

    @staticmethod
    async def my_ranking(rank:RankingUpdate,user_id:int,
                   db: AsyncSession):
        # user_id 가 있는지 확인 (예외 처리)
        # RankingCrud.update_ranking 실행
        # 새로운 랭킹 예외 처리 후 반환
        pass

    @staticmethod
    async def top_10_rank(user_id:int,db: AsyncSession):
        # user_id 가 있는지만 확인
        # RankingCrud.get_top10_rank 를 실행
        # 그대로 10개 리턴
        pass