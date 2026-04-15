from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.balance import Balance
from sqlalchemy.future import select
from app.db.crud.balance import BalanceCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.scheme.balance import BalanceUpdate



class BalanceService:

    @staticmethod
    async def update_my_balance(user_id:str,db:AsyncSession):
        # user_id 가 있는지 확인 (예외처리)
        # BalanceCrud.get_last_trade 를  user_id 넣고 실행
        # BalanceCrud.update_my_balance 를 위 행을 넣고 실행
        # BalanceCrud.update_my_money 를 위에서 뽑은 balance 객체에서 수량, 매입단가, 평가금액을 넣고 실행 
        pass


    @staticmethod
    async def my_balance(user_id:str,db:AsyncSession):
        # user_id 가 있는지 확인 (예외처리)
        # BalanceCrud.get_by_id 를 실행
        # 그대로 리스트 반환
        pass