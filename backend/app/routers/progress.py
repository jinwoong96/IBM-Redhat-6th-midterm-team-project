from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.progress import ProgressService
from app.core.auth import get_current_user


router = APIRouter(prefix="/progress", tags=["progress"])

@router.put("/",)
async def next(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # ProgressService.next 를 실행
    pass