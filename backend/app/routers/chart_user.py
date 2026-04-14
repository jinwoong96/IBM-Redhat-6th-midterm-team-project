from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.chart_user import ChartuserService
from app.core.auth import get_current_user
from app.db.scheme.chart_user import ChartuserGet,ChartuserUpdate



router = APIRouter(prefix="/chartuser", tags=["chartuser"])


@router.get("/{up_date}",)
async def get_chartuser(up_date:int,chart:ChartuserGet,current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # ChartuserService.get_chartuser 실행 후 Chartuser 리스트 반환
    pass

@router.post("/",)
async def add_chartuser(chart:ChartuserUpdate,current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # ChartuserService.add_chartuser 실행 후 메세지 리턴
    pass