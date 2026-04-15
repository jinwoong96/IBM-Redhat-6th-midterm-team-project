from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.user import User
from app.db.scheme.user import UserRequest, UserUpdate



class UserCrud:
    
    @staticmethod
    async def new_user(user:UserRequest,db:AsyncSession):
        # service 에서 받은 user 정보로 db에 add
        # 그 유저를 그대로 리턴
        pass


    @staticmethod
    async def get_by_id(user_id:str,db:AsyncSession):
        # 아이디에 해당하는 튜플 빼고 리턴
        pass

    @staticmethod
    async def update_refresh_token_by_id(user_id:str,
        refresh_token:str,
        db:AsyncSession):
    # 해당 유저의 리프레시토큰을 업데이트 (flush)
        pass

    @staticmethod
    async def get_all(db:AsyncSession):
        # 모든 유저 뽑아서 반환
        pass

    @staticmethod
    async def update_by_id(user_id:str,userupdate:UserUpdate,db:AsyncSession):
        # user_id 에 맞는 튜플 뽑기( 로그인된 유저 )
        # 그 튜플에 입력한 userupdate 데이터를 삽입
        # flush
        # 업데이트된 유저 정보 반환
        pass
    @staticmethod
    async def delete_by_id(user_id:str,db:AsyncSession):
        # user_id 에 해당되는 튜플 뽑음
        # db.delete , flush
        # 삭제를 성공하면 삭제 했다는 메세지 리턴
        pass