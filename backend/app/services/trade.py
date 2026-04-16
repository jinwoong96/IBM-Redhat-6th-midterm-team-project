from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.trade import Trade
from sqlalchemy.future import select
from app.db.crud.trade import TradeCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.scheme.trade import TradeCreate

class TradeService:

    @staticmethod
    async def my_trade_list(login_id:str, limit:int, offset:int, db:AsyncSession):
        pass

    @staticmethod
    async def new_trade(login_id:str,trade:TradeCreate,db:AsyncSession):
        pass