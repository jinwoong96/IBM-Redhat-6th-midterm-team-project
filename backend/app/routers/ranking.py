from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.scheme.ranking import RankingUpdate
from app.services.ranking import RankingService
from app.core.auth import get_current_user


router = APIRouter(prefix="/ranking", tags=["ranking"])


@router.get("",)
async def top_10_rank(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # RankingService.top_10_rank 실행
    pass

@router.get("/me",)
async def my_ranking(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # RankingService.my_ranking 을 실행
    pass