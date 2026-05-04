from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.user import User
from app.db.scheme.user import UserCreate, UserUpdate
from app.core.jwt_handle import get_password_hash



class UserCrud:
    
    @staticmethod
    async def create(user:UserCreate, db:AsyncSession):
        user_data=user.model_dump()
        user_data['user_password']=get_password_hash(user_data['user_password'])

        db_user=User(**user_data)
        db.add(db_user)
        await db.flush()
        return db_user


    @staticmethod
    async def get_by_login_id(login_id:str, db:AsyncSession):
        result=await db.execute(select(User).filter(User.login_id==login_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_refresh_token_by_id(login_id:str,
        refresh_token:str,
        db:AsyncSession):
        
        db_user = await db.get(User, login_id)
        if db_user:
            db_user.refresh_token = refresh_token
            await db.flush()
        return db_user


    @staticmethod
    async def update_by_id(login_id:str, userupdate:UserUpdate, db:AsyncSession):
        db_user = await db.get(User, login_id)
        if db_user:
            update_data = userupdate.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_user, key, value)
            await db.flush()
            return db_user
        return None
    
    @staticmethod
    async def get_user_by_login_id(login_id: str, db: AsyncSession):
        result = await db.execute(select(User).filter(User.login_id == login_id))
        return result.scalars().first()
    
    @staticmethod
    async def get_by_nickname(nickname: str, db: AsyncSession):
        result = await db.execute(select(User).filter(User.user_nickname == nickname))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update_valuation(user: User, new_valuation: int, db: AsyncSession) -> User:
        user.valuation = new_valuation
        await db.flush()
        return user