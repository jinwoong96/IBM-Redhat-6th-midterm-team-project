from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.models.user import User
from app.db.scheme.user import UserCreate, UserLogin, UserUpdate
from app.db.crud.user import UserCrud
from fastapi import HTTPException
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token, create_refresh_token
from app.core.settings import settings
from fastapi import Response


class UserService:

    @staticmethod
    async def signup(user:UserCreate, db:AsyncSession):
        if await UserCrud.get_by_login_id(user.login_id, db):
            raise HTTPException(status_code=400,  detail="이미 사용중인 아이디")

        try:
            db_user=await UserCrud.create(user, db)
            await db.commit()
            await db.refresh(db_user)
            return db_user
        
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")


    @staticmethod
    async def login(user:UserLogin, response:Response, db:AsyncSession):
        db_user=await UserCrud.get_by_login_id(user.login_id.strip(), db)
        
        if not db_user:
            print("❌ 유저 없음")
            raise HTTPException(status_code=401, detail="잘못된 아이디 또는 비번")
    
        if not verify_password(user.user_password, db_user.user_password):
         raise HTTPException(status_code=401, detail="잘못된 아이디 또는 비번")

        login_id=db_user.login_id
        access_token=create_access_token(login_id)
        refresh_token=create_refresh_token(login_id)

        try:
            await UserCrud.update_refresh_token_by_id(login_id, refresh_token, db)
            await db.commit()
            await db.refresh(db_user)

            response.set_cookie(
            key="access_token",
            value=access_token,
            max_age=int(settings.access_token_expire_seconds),
            secure=False,
            httponly=True,
            samesite="Lax",
            )

            response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            max_age=int(settings.refresh_token_expire_seconds),
            secure=False,
            httponly=True,
            samesite="Lax",
            )
            
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"토큰 저장 실패: {str(e)}")

        return {'access_token':access_token, 'token_type':'bearer', 
                "user": {
                "login_id": db_user.login_id,
                "user_nickname": db_user.user_nickname,
                "money": db_user.money,
                "valuation": db_user.valuation,
                "created_at": db_user.created_at
                }}

    @staticmethod
    async def get_user(login_id:str, db:AsyncSession):
        db_user = await UserCrud.get_by_login_id(login_id, db)
        if not db_user:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없음")
        return db_user

    @staticmethod
    async def update_user(login_id:str, userupdate:UserUpdate, db:AsyncSession):
        db_user = await UserCrud.get_by_login_id(login_id, db)
        if not db_user:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없음")

        # 닉네임이 있고 공백이 아닐 때만 업데이트
        if userupdate.user_nickname and userupdate.user_nickname.strip():
            db_user.user_nickname = userupdate.user_nickname.strip()

        # 새 비밀번호가 있고 공백이 아닐 때만 업데이트
        if userupdate.new_password and userupdate.new_password.strip():
            db_user.user_password = get_password_hash(userupdate.new_password)

        await db.commit()
        await db.refresh(db_user)
        return db_user
        
    @staticmethod
    async def check_duplicate(login_id: str = None, nickname: str = None, db: AsyncSession = None):
        if login_id:
            if await UserCrud.get_by_login_id(login_id, db):
                raise HTTPException(status_code=409, detail="이미 사용 중인 아이디입니다.")
        if nickname:
            if await UserCrud.get_by_nickname(nickname, db):
                raise HTTPException(status_code=409, detail="이미 사용 중인 닉네임입니다.")
        return True

    @staticmethod
    async def delete_user(login_id: str, password: str, db: AsyncSession):
        db_user = await UserCrud.get_by_login_id(login_id, db)
        if not db_user or not verify_password(password, db_user.user_password):
            raise HTTPException(status_code=401, detail="비밀번호가 일치하지 않습니다.")
        
        try:
            await UserCrud.delete(db_user, db)
            await db.commit()
            return True
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"탈퇴 처리 중 오류 발생: {str(e)}")
