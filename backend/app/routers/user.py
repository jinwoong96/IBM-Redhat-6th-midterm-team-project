from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.scheme.user import UserRequest, UserUpdate
from app.services.user import UserService
from app.core.auth import get_current_user
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/",)
async def create_user(user: UserRequest, db: AsyncSession = Depends(get_db)):
# 사용자 생성 
# UserService.signup
    pass

@router.post("/token",)
async def login(user: UserRequest, db: AsyncSession = Depends(get_db)):
# UserService.login 을 정보 다주고 시작
    pass

@router.get("/me",)
async def me(current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # current_user 로 로그인이 되있으면 그 유저 튜플을 그대로 반환(User)
    # current_user.user_id로 UserService.get_user 에 넣어 유저 반환
    pass

@router.get("/",)
async def all_users(db: AsyncSession = Depends(get_db)):
    # UserService.get_all_users 로 모든 유저 반환
    pass

@router.get("/{user_id}",)
async def get_user(user_id:str,
                   current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # UserService.get_user_2(user_id,current_user.user_id,db) 유저 가져옴
    pass

@router.put("/",)
async def update_user(userupdate:UserUpdate,current_user= Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)):
    # UserService.update_user 로 업데이트 된 유저 바로 리턴
    pass
@router.delete("/{user_id}",)
async def delete_user(user_id:str,current_user= Depends(get_current_user),
                   db: AsyncSession = Depends(get_db)):
    # UserService.delete_user 로 바로리턴
    pass

@router.get("/check",)
async def dup_check(user_id:str,db: AsyncSession = Depends(get_db)):
    # UserService.dup_check 로 user_id 넘김
    # 반환된 메세지를 저장해 그대로 출력
    # user_id 쿼리파라미터임
    pass