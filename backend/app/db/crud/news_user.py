from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.news_user import NewsUser
from app.db.models.news import News
import random


class NewsuserCrud:

    @staticmethod
    async def get_by_login_id(login_id:str,db:AsyncSession):
        query=select(NewsUser).filter_by(login_id=login_id)
        result=await db.execute(query)
        return result.scalars().all()
    


    @staticmethod
    async def create(login_id:str,news_id:int,day:int,db:AsyncSession):
        news_record=NewsUser(
            login_id=login_id,
            news_id=news_id,
            day=day
        )
        db.add(news_record)
        return news_record