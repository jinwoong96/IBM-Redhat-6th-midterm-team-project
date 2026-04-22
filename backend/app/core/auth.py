from fastapi import Request,Response,HTTPException,Depends
from app.core.settings import settings
# from app.core.jwt_handle import verify_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.crud.user import UserCrud
from fastapi.security import OAuth2PasswordBearer

# 토큰 url 지정


async def get_current_user(request:Request,token:str,db: AsyncSession = Depends(get_db)):
    # 쿠키에서 access_token 을 가져옴 (예외처리)
    # 토큰 decode 해서 login_id를뺌
    # 그 login_id 를 UserCrud.get_by_id 로 해당 튜플 조회(예외처리)
    # 해당 유저 그대로 반환
    
    pass