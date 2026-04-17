from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.scheme.user import UserCreate, UserLogin, UserUpdate
from app.services.user import UserService
from app.core.auth import get_current_user
router = APIRouter(prefix="/users", tags=["users"])

@router.post("",)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
# 사용자 생성 
# UserService.signup
    pass

@router.post("/token",)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
# UserService.login 을 정보 다주고 시작
    pass

@router.get("/me",)
async def me(current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # current_user 로 로그인이 되있으면 그 유저 튜플을 그대로 반환(User)
    # current_user.user_id로 UserService.get_user 에 넣어 유저 반환
    pass

@router.put("",)
async def update_user(userupdate:UserUpdate,current_user= Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)):
    # UserService.update_user 로 업데이트 된 유저 바로 리턴
    pass
