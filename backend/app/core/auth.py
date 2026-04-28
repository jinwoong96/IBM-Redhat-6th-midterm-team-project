from fastapi import Request, Response, HTTPException, Depends
from typing import Optional
# from app.core.settings import settings
from app.core.jwt_handle import verify_token, create_access_token, create_refresh_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.crud.user import UserCrud
from jwt import ExpiredSignatureError, InvalidTokenError, InvalidSignatureError
from app.core.settings import settings

# 토큰 url 지정

def set_auth_cookies(response:Response, access_token:str, refresh_token:str) -> None:
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=int(settings.access_token_expire_seconds),
        secure=False,
        httponly=True,
        samesite="lax"
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=int(settings.refresh_token_expire_seconds),
        secure=False,
        httponly=True,
        samesite="lax"
    )

def clear_auth_cookies(response:Response)->None:
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')


async def get_current_user(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db)
) -> str:
    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")

    # 1. access_token이 있으면 먼저 검증
    if access_token:
        try:
            login_id = verify_token(access_token)
            return login_id

        except ExpiredSignatureError:
            # access 만료면 아래 refresh 로직으로 내려감
            pass

        except InvalidTokenError:
            raise HTTPException(status_code=401, detail="액세스 토큰이 유효하지 않음")

    # 2. access_token이 없거나 만료된 경우 refresh_token 확인
    if not refresh_token:
        raise HTTPException(status_code=401, detail="토큰이 없음")

    try:
        login_id = verify_token(refresh_token)

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰이 만료됨")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="토큰이 유효하지 않음")

    # 3. DB refresh token과 비교
    user = await UserCrud.get_by_login_id(login_id, db)

    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없음")

    if user.refresh_token != refresh_token:
        raise HTTPException(status_code=401, detail="토큰이 일치하지 않음")

    # 4. 새 토큰 발급
    new_access_token = create_access_token(login_id)
    new_refresh_token = create_refresh_token(login_id)

    try:
        await UserCrud.update_refresh_token_by_id(
            login_id,
            new_refresh_token,
            db
        )
        await db.commit()

    except Exception:
        await db.rollback()
        raise HTTPException(status_code=500, detail="토큰 재발급 실패")

    # 5. 새 쿠키 심기
    set_auth_cookies(response, new_access_token, new_refresh_token)

    return login_id

    
async def get_optional(request:Request) -> Optional[int]:
    access_token = request.cookies.get("access_token")
    if not access_token:
        return None
    try:
        return verify_token(access_token)
    except (ExpiredSignatureError, InvalidSignatureError):
        return None