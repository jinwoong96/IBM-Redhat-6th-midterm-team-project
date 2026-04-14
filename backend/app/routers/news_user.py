from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.scheme.news_user import NewsuserAdd
from app.services.news_user import NewsuserService
from app.core.auth import get_current_user

router = APIRouter(prefix="/newsuser", tags=["newsuser"])


@router.get("/",)
async def my_newsuser(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # NewsuserService.my_newsuser 를 실행
    pass


@router.post("/",)
async def add_newsuser(news:NewsuserAdd,current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # NewsuserService.add_newsuser 를 실행
    pass