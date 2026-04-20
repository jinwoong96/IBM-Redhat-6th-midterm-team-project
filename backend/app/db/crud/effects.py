from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.effects import Effects

class EffectsCrud:
    @staticmethod
    async def get_by_news_id(news_id:int, db:AsyncSession):
        