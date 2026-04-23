from fastapi import Request, Response, HTTPException, Depends
from typing import Optional
# from app.core.settings import settings
from app.core.jwt_handle import verify_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.crud.user import UserCrud
# from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidSignatureError

# 토큰 url 지정

def clear_auth_cookies(response:Response)->None:
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')


async def get_current_user(request:Request, db:AsyncSession=Depends(get_db)):
    # 쿠키에서 access_token 을 가져옴 (예외처리)
    # 토큰 decode 해서 login_id를뺌
    # 그 login_id 를 UserCrud.get_by_id 로 해당 튜플 조회(예외처리)
    # 해당 유저 그대로 반환

    access_token=request.cookies.get('access_token')

    if not access_token:
        raise HTTPException(status_code=401, detail='액세스 토큰 없음')

    try:
        login_id = verify_token(access_token)

        if login_id is None:
            raise HTTPException(status_code=401, detail='유효하지 않은 토큰')

        try:
            user = await UserCrud.get_by_login_id(login_id, db)
            if not user:
                raise HTTPException(status_code=404, detail='찾을 수 없는 사용자')
            return login_id
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'유저 조회 실패:{str(e)}')
    
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='엑세스 토큰 만료. 다시 로그인 해 주세요.')
    
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail='유효하지 않은 엑세스 토큰')
    
async def get_optional(request:Request) -> Optional[int]:
    access_token = request.cookies.get("access_token")
    if not access_token:
        return None
    try:
        return verify_token(access_token)
    except (ExpiredSignatureError, InvalidSignatureError):
        return None