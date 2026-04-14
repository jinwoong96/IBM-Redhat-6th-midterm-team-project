from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.news_user import Newsuser
from app.db.scheme.news_user import NewsuserAdd
from sqlalchemy.future import select
from app.db.crud.news_user import NewsuserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class NewsuserService:

    @staticmethod
    async def my_newsuser(user_id:int,db:AsyncSession):
        # user_id가 있는지 확인(에러처리)
        # NewsuserCrud.get_by_id 로 리스트 반환
        pass

    @staticmethod
    async def add_newsuser(user_id:int,news:NewsuserAdd,db:AsyncSession):
        # user_id 있는지 확인(에러처리)
        # NewsuserCrud.new_newsuser 실행
        # 생성된 뉴스를 반환
        pass