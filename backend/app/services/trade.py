from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.trade import Trade
from sqlalchemy.future import select
from app.db.crud.trade import TradeCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.scheme.trade import TradeCreate

# from app.services.balance import BalanceService 

class TradeService:

    @staticmethod
    async def my_trade_list(login_id: str, limit: int, offset: int, db: AsyncSession):        
        return await TradeCrud.get_list_by_login_id(login_id, limit, offset, db)

    @staticmethod
    async def new_trade(login_id: str, trade_data: TradeCreate, db: AsyncSession):
        if trade_data.buy_type not in ("buy", "sell"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="buy_type은 'buy' 또는 'sell' 이어야 합니다."
            )

        try:
            
            new_trade = await TradeCrud.create(login_id, trade_data, db)
            
            await db.commit()
            await db.refresh(new_trade)
            return new_trade
            
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=400, detail=str(e))