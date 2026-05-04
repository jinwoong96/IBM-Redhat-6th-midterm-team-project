from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.trade import Trade
from app.db.models.item import Item
from app.db.scheme.trade import TradeCreate

class TradeCrud:

    @staticmethod
    async def get_list_by_login_id(login_id: str, limit: int, offset: int, db: AsyncSession):
        stmt = (
            select(
                Trade.trade_day,
                Trade.trade_id,
                Item.item_name,
                Trade.login_id,
                Trade.item_code,
                Trade.buy_type,
                Trade.price,
                Trade.quantity
            )
            .join(Item, Trade.item_code == Item.item_code)
            .where(Trade.login_id == login_id)
            .order_by(Trade.trade_id.desc())  # trade_day가 단계 단위이므로 고유 id 역순이 최신순
            .offset(offset)
            .limit(limit)
        )
        
        result = await db.execute(stmt)
        return result.mappings().all()

    @staticmethod
    async def create(login_id: str, trade_data: TradeCreate, db: AsyncSession):
        db_trade = Trade(
            login_id=login_id,
            item_code=trade_data.item_code,
            buy_type=trade_data.buy_type,
            price=trade_data.price,
            quantity=trade_data.quantity,
            trade_day=trade_data.trade_day  # schema에서 받아온 단계 삽입
        )
        db.add(db_trade)
        await db.flush() 
        return db_trade