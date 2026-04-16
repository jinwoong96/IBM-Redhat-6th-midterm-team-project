from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.ranking import Ranking
from app.db.scheme.ranking import RankingUpdate
from sqlalchemy.future import select
from app.db.crud.ranking import RankingCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class RankingService:

    @staticmethod
    async def my_ranking(login_id:str,
                   db: AsyncSession):
        pass

    @staticmethod
    async def top_10_rank(login_id:str,db: AsyncSession):
        pass