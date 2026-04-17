from fastapi import APIRouter, Depends, Response, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.db.database import get_db
from app.services.chart_user import ChartuserService
from app.core.auth import get_current_user
from app.db.scheme.chart_user import ChartuserGet,ChartuserUpdate



router = APIRouter(prefix="/chartuser", tags=["chartuser"])


@router.get("/items/{item_code}",)
async def get_chartuser(item_code:Annotated[str,Path(...)], limit:Annotated[int,Query(ge=1)]=20,
            current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # ChartuserService.get_chartuser 실행 후 Chartuser 리스트 반환
    pass

@router.post("/init",)
async def add_chartuser(current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # ChartuserService.init_chartuser 실행 후 메세지 리턴
    pass

@router.get("/items",)
async def get_itemlist(current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # ChartuserService.get_itemlist 실행 후 메세지 리턴
    pass