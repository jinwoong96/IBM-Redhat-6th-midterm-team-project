from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.news_user import Newsuser
from app.db.scheme.news_user import NewsuserAdd

class NewsuserCrud:

    @staticmethod
    async def get_by_id(user_id:int,db:AsyncSession):
        # user_id 에 맞는 모든 행을 리스트로 반환
        pass

    @staticmethod
    async def new_newsuser(user_id:int,news:NewsuserAdd,db:AsyncSession):
        # 입력 데이터에 맞는 새 뉴스를 생성 및 db.add
        # 새 뉴스 반환
        pass