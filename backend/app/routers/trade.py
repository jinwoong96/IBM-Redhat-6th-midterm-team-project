from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, List
from app.db.database import get_db
from app.services.trade import TradeService
from app.core.auth import get_current_user
from app.db.scheme.trade import TradeCreate, TradeResponse,TradeHistoryResponse
from app.services.balance import BalanceService
router = APIRouter(prefix="/trade", tags=["trade"])

@router.post("", response_model=TradeResponse)
async def new_trade(
    trade: TradeCreate,
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    
    login_id = current_user
    return await TradeService.new_trade(login_id, trade, db)


@router.get("", response_model=List[TradeHistoryResponse]) 
async def my_trade_list(
    limit: Annotated[int, Query(ge=1)] = 100, 
    offset: Annotated[int, Query(ge=0)] = 0, 
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    login_id = current_user 
    return await TradeService.my_trade_list(login_id, limit, offset, db)

@router.get("/count")
async def my_trade_count(
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await TradeService.get_trade_count(current_user, db)