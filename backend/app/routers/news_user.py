from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.db.database import get_db
from app.db.scheme.news_user import NewsuserAdd
from app.services.news_user import NewsuserService
from app.core.auth import get_current_user

router = APIRouter(prefix="/newsuser", tags=["newsuser"])


@router.get("",)
async def my_newsuser(limit:Annotated[int,Query(ge=1)]=15, current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # NewsuserService.my_newsuser 를 실행
    pass


@router.post("/generate",)
async def add_newsuser(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # NewsuserService.add_newsuser 를 실행
    pass