from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated ,List
from app.db.database import get_db
from app.db.scheme.news_user import NewsUserRead
from app.db.scheme.news import NewsRead
from app.services.news_user import NewsuserService
from app.core.auth import get_current_user

router = APIRouter(prefix="/newsuser", tags=["newsuser"])


@router.get("",response_model=List[NewsUserRead])#인증된 사용자의 과거뉴스기록
async def my_newsuser(limit:Annotated[int,Query(ge=1)]=15, current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    
    history = await NewsuserService.my_newsuser(
        login_id=current_user, 
        limit=limit, 
        db=db
    )
    return history


@router.post("/generate",response_model=NewsRead)#사용자에게 뉴스배정 및 기록
async def add_newsuser(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    
    new_random_news=await NewsuserService.add_newsuser(
        login_id=current_user,
        db=db
    )
    return new_random_news   #차트유저 더미데이터가 없으면 에러가남 