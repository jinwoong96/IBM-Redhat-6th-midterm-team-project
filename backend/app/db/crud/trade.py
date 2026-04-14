from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.trade import Trade
from app.db.scheme.trade import TradeUpdate

class TradeCrud:

    @staticmethod
    async def get_my_tradelist(user_id:int,db:AsyncSession):
        # user_id가 맞는 모든 행을 리스트로 뽑음
        # 반환
        pass

    @staticmethod
    async def new_trade(user_id:int,trade:TradeUpdate,db:AsyncSession):
        # 입력한 정보로 새 trade 생성
        # db에 add
        # 그 유저 그대로 리턴
        pass