from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.balance import Balance
from sqlalchemy.future import select
from app.db.crud.balance import BalanceCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
from app.db.scheme.balance import BalanceUpdate



class BalanceService:
    @staticmethod
    async def my_balance(login_id:str,db:AsyncSession):
        pass