from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.news_user import NewsUser
from app.db.models.news import News
import random
from sqlalchemy.orm import joinedload
from sqlalchemy import desc


class NewsuserCrud:

    @staticmethod
    async def get_by_login_id(login_id:str,limit:int,db:AsyncSession):
        # query=select(NewsUser).filter(NewsUser.login_id==login_id)
        result=await db.execute(
            select(NewsUser).options(joinedload(NewsUser.news)).filter(NewsUser.login_id==login_id).order_by(desc(NewsUser.news_user_id)).limit(limit)#로그인 아이디로 지난 뉴스기록가져올때 테이블에 조인해서 제목/내용까지 가져오게
        )
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