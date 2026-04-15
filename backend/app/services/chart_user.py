from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.chart_user import ChartUser
from sqlalchemy.future import select
from app.db.crud.chart_user import ChartuserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.scheme.chart_user import ChartuserUpdate,ChartuserGet
class ChartuserService:

    @staticmethod
    async def get_chartuser(up_date:int,user_id:str,current_user_id:str,db:AsyncSession):
        # current_user_id가 있는지 확인 (예외처리)
        # WishlistCrud.get_by_id_ud 로 날짜와 user_id 다넘겨줘야함
        # 리스트를 받아서 그대로 반환 
        pass

    @staticmethod
    async def add_chartuser(user_id:str,chart:ChartuserUpdate,db:AsyncSession):
        # user_id 잇는지 확인 (예외처리)
        # WishlistCrud.new_chartuser 로 입력 데이터를 전부 넘겨줘서 db에 등록
        # 리턴 받은 새 chartuser를 커밋-리프레시(예외 처리)
        # 메세지리턴
        pass