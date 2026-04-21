from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.trade import Trade
from app.db.scheme.trade import TradeCreate

class TradeCrud:

    @staticmethod
    async def get_list_by_login_id(login_id: str, limit: int, offset: int, db: AsyncSession):
        result = await db.execute(
            select(Trade)
            .filter(Trade.login_id == login_id)
            .offset(offset)
            .limit(limit)
        )
        return result.scalars().all()

    @staticmethod
    async def create(login_id: str, trade_data: TradeCreate, db: AsyncSession):
        db_trade = Trade(
            login_id=login_id,
            item_code=trade_data.item_code,
            buy_type=trade_data.buy_type,
            price=trade_data.price,
            quantity=trade_data.quantity
        )
        db.add(db_trade)
        await db.flush() # ID 등 확보를 위해 flush
        return db_trade