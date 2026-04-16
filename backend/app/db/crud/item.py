from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.item import Item


class ItemCrud:

    @staticmethod
    async def get_all_item(db:AsyncSession):
        # 모든 종목을 꺼내서 반환
        pass
