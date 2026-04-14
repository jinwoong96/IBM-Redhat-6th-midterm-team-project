from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.item import ItemService
from app.core.auth import get_current_user

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/all",)
async def all_item(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # ItemService.all_item(user_id,db) 로 모든 아이템 반환
    pass

@router.get("/",)
async def top_10_item(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # ItemService.top_10_item(user_idmdb) 로 등락폭 10위 아이템 반환
    pass