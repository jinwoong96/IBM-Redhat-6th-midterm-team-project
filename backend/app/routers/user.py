from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.scheme.user import UserCreate, UserLogin, UserUpdate, TokenResponse, UserInfo, UserDelete
from app.services.user import UserService
from app.core.auth import get_current_user
router = APIRouter(prefix="/users", tags=["users"])
from typing import Optional, Annotated

# 회원가입
@router.post("", response_model=UserCreate)
async def create_user(user:UserCreate, db:AsyncSession=Depends(get_db)):
# 사용자 생성 
# UserService.signup
    return await UserService.signup(user, db)

# 로그인
@router.post("/token", response_model=TokenResponse)
async def login(user:UserLogin, response:Response, db:AsyncSession=Depends(get_db)):
# UserService.login 을 정보 다주고 시작
    result = await UserService.login(user, response, db)
    
    response.set_cookie(
        key='access_token',
        value=result['access_token'],
        httponly=True,
        samesite='lax'
    )
    return result

# 로그인된 사용자 정보 조회
@router.get("/me", response_model=UserInfo)
async def me(current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)): ## 이중 세션이라는데 db를 지워도 될지?
    # current_user 로 로그인이 되있으면 그 유저 튜플을 그대로 반환(User)
    # current_user.user_id로 UserService.get_user 에 넣어 유저 반환
    return await UserService.get_user(current_user, db)

# 로그인된 사용자 정보 수정
@router.put("", response_model=UserUpdate)
async def update_user(userupdate:UserUpdate, current_user=Depends(get_current_user),
                      db:AsyncSession=Depends(get_db)):
    # UserService.update_user 로 업데이트 된 유저 바로 리턴
    return await UserService.update_user(current_user, userupdate, db)

# 로그아웃
@router.post("/logout", response_model=bool)
async def logout(response:Response):
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return True

# 아이디/닉네임 중복 체크
@router.get("/check-duplicate")
async def check_duplicate(
    login_id: Annotated[str, Query(min_length=1)] = None, 
    nickname: Annotated[str, Query(min_length=1)] = None, 
    db: AsyncSession = Depends(get_db)
):
    return await UserService.check_duplicate(login_id=login_id, nickname=nickname, db=db)

# 회원 탈퇴 (계정 삭제)
@router.delete("", response_model=bool)
async def delete_user(delete_data:UserDelete, response:Response,
                      current_user=Depends(get_current_user), db:AsyncSession=Depends(get_db)):
    result = await UserService.delete_user(current_user, delete_data.password, db)
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return result