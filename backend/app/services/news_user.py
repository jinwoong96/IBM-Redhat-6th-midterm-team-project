from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.crud.news import NewsCrud
from app.db.crud.news_user import NewsuserCrud
from app.db.crud.effects import EffectsCrud
from app.db.models.news import News
import random
class NewsuserService:

    @staticmethod #사용자의 과거뉴스기록 조회
    async def my_newsuser(login_id:str,limit:int, db:AsyncSession): #해당유저의 전체기록조회
        history=await NewsuserCrud.get_by_login_id(login_id,db)

        if not history: #예외 : 기록이 없을때 (1일차)
            return []
        
        history.sort(key=lambda x:x.day, reverse=True)
        return history[:limit]




    @staticmethod
    async def add_newsuser(login_id:str,db:AsyncSession): #새로운 날짜의 뉴스를 랜덤배정 후 기록
        seen_news_id=await NewsuserCrud.get_by_login_id(login_id,db) #사용자가 지금까지 본 뉴스 아이디 리스트

        all_news=await NewsCrud.get_all_news(db)#모든뉴스를 가져와서
        unseen_news=[n for n in all_news if n.news_id not in seen_news_id]#안본 뉴스중 하나를 고른다

        if not unseen_news:
            raise HTTPException(status_code=404,detail='새로운 뉴스가 없습니다')#만약 뉴스가 더없다면..
        
        select_random_news=random.choice(unseen_news)#랜덤으로 뉴스를 뽑는다

        await NewsuserCrud.create(#새로 배정된 뉴스를 db에저장 근데 이거 다음날 뉴스라서 저장할때 +1이 맞지않나?
            login_id=login_id,
            news_id=select_random_news.news_id,
            day=1,
            db=db
        )
        await db.commit()

        return select_random_news

