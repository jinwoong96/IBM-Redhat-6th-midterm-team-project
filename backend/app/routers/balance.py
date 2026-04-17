from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.balance import BalanceService
from app.core.auth import get_current_user

router = APIRouter(prefix="/balance", tags=["balance"])


@router.get("/",)
async def my_balance(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # BalanceService.my_balance 실행
    pass