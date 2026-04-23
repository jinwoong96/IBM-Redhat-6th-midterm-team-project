from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.scheme.user import UserCreate, UserLogin, UserUpdate, TokenResponse
from app.services.user import UserService
from app.core.auth import get_current_user
router = APIRouter(prefix="/users", tags=["users"])

# 회원가입
@router.post("", response_model=UserCreate)
async def create_user(user:UserCreate, db:AsyncSession=Depends(get_db)):
# 사용자 생성 
# UserService.signup
    return await UserService.signup(user, db)

# 로그인
@router.post("/token", response_model=TokenResponse)
async def login(user:UserLogin, response:Response, db: AsyncSession= Depends(get_db)):
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
@router.get("/me", response_model=UserLogin)
async def me(current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)): ## 이중 세션이라는데 db를 지워도 될지?
    # current_user 로 로그인이 되있으면 그 유저 튜플을 그대로 반환(User)
    # current_user.user_id로 UserService.get_user 에 넣어 유저 반환
    return await UserService.get_user(current_user, db)

# 로그인된 사용자 정보 수정
@router.put("", response_model=UserUpdate)
async def update_user(userupdate:UserUpdate, current_user=Depends(get_current_user),
                      db: AsyncSession=Depends(get_db)):
    # UserService.update_user 로 업데이트 된 유저 바로 리턴
    return await UserService.update_user(current_user, userupdate, db)
