from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.trade import Trade
from sqlalchemy.future import select
from app.db.crud.trade import TradeCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.scheme.trade import TradeCreate

class TradeService:

    @staticmethod
    async def my_trade_list(user_id:str,db:AsyncSession):
        # user_id 가 있는지 확인(에러 처리)
        # TradeCrud.get_my_tradelist 로 내 체결내역 리스트 반환
        pass

    @staticmethod
    async def new_trade(user_id:str,trade:TradeCreate,db:AsyncSession):
        # user_id 가 있는지 확인(에러 처리)
        # TradeCrud.new_trade 로 새 체결내역 생성 후 db에 add
        # 커밋 리프레시
        pass