from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.db.database import get_db
from app.services.trade import TradeService
from app.core.auth import get_current_user
from app.db.scheme.trade import TradeCreate
from app.services.balance import BalanceService
router = APIRouter(prefix="/trade", tags=["trade"])

@router.post("",)
async def new_trade(trade:TradeCreate,current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # TradeService.new_trade 를 실행
    pass


@router.get("",)
async def my_trade_list(limit:Annotated[int,Query(ge=1)]=100, offset:Annotated[int,Query(ge=0)]=0, 
             current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # TradeService.my_trade_list 를 실행
    pass