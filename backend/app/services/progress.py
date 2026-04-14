from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.db.scheme.user import UserRequest,UserUpdate
from sqlalchemy.future import select
from app.db.crud.user import UserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token


class ProgressService:

    @staticmethod
    async def next(user_id:int,db:AsyncSession):
        # user_id가 있는지 확인 (예외 처리)
        # ProgressCrud.get_by_id_balance 를실행
        # 리턴된 종목코드 리스트, user_id를 가지고 아래 
        # ProgressCrud.get_by_id_chart 를 실행
        # ProgressCrud.next_update 에 end_price를 넣고 실행

        pass