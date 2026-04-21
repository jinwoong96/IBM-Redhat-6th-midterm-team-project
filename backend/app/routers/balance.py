from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.balance import BalanceService
from app.core.auth import get_current_user
from app.db.scheme.balance import BalanceUpdate
from typing import List
router = APIRouter(prefix="/balance", tags=["balance"])


@router.get("",response_model=List[BalanceUpdate])
async def my_balance(current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    login_id = current_user.login_id
    return await BalanceService.my_balance(login_id,db)
    
  