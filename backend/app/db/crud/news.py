from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,func
from app.db.models.news import News
import random

class NewsCrud:
    @staticmethod
    async def get_news_id(news_id:int,db:AsyncSession):
        result=await db.execute(select(News).filter_by(news_id=news_id))
        return result.scalar_one_or_none()
    
    @staticmethod #관리자용
    async def get_all_news(db:AsyncSession):
        result=await db.execute(select(News))
        return result.scalars().all()
        




   