from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.ranking import Ranking
from app.db.scheme.ranking import RankingResponse, Top10Response
from sqlalchemy.future import select
from sqlalchemy import func
from app.db.crud.ranking import RankingCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token

class RankingService:

    @staticmethod
    async def my_ranking(login_id:str,
                   db: AsyncSession):
        ranking = await RankingCrud.get_by_login_id(
            login_id=login_id,
            db=db
        )
        total_count = await RankingCrud.get_all_count(db=db)
        if not ranking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="내 랭킹 정보가 없습니다."
            )

        result = await db.execute(
            select(func.count())
            .select_from(Ranking)
            .filter(Ranking.max_accounts > ranking.max_accounts)
        )
        higher_count = result.scalar()

        response = RankingResponse(
            login_id=ranking.login_id,
            user_nickname=ranking.user.user_nickname,
            max_accounts=ranking.max_accounts,
            max_plus=ranking.max_plus,
            day=ranking.day,
            rank=higher_count + 1
        )

        return {"my_ranking" : response,
                "total_user":total_count}

    @staticmethod
    async def get_top10_rank(db: AsyncSession):
        rankings = await RankingCrud.get_top10_rank(db=db)

        if not rankings:
            return []
        
        response = [
            Top10Response(
                rank=i + 1,
                login_id=r.login_id,
                user_nickname=r.user.user_nickname,
                max_accounts=r.max_accounts
            )
            for i, r in enumerate(rankings)
        ]
        
        return response