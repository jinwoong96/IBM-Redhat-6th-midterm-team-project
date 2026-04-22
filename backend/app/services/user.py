from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.models.user import User
from app.db.scheme.user import UserCreate, UserLogin, UserUpdate
from app.db.crud.user import UserCrud
from fastapi import HTTPException
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token, create_refresh_token



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
        
        except Exception:
            raise HTTPException(status_code=401, detail="잘못된 아이디 또는 비번")


    @staticmethod
    async def login(user:UserLogin, db:AsyncSession):
        db_user=await UserCrud.get_by_login_id(user.login_id, db)
        if not db_user or not verify_password(user.user_password, db_user.user_password):
            raise HTTPException(status_code=401, detail="잘못된 아이디 또는 비번")

        login_id=db_user.login_id
        refresh_token=create_refresh_token(login_id)
        access_token=create_access_token(login_id)

        await UserCrud.update_refresh_token_by_id(login_id, refresh_token, db)
        await db.commit()
        await db.refresh(db_user)

        return db_user, access_token, refresh_token

    @staticmethod
    async def get_user(login_id:str, db:AsyncSession):
        db_user = await UserCrud.get_by_id(login_id, db)
        if not db_user:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없음")
        return db_user

    @staticmethod
    async def update_user(login_id:str, userupdate:UserUpdate, db:AsyncSession):
        if userupdate.user_password:
            hash_pw=get_password_hash(userupdate.user_password)
            userupdate.user_password = hash_pw

        db_user=await UserCrud.update_by_id(login_id, userupdate, db)

        if not db_user:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없음")
        
        await db.commit()
        await db.refresh(db_user)
        
        return db_user
