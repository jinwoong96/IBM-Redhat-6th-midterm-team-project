from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.db.scheme.user import UserRequest,UserUpdate
from sqlalchemy.future import select
from app.db.crud.user import UserCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token



class UserService:

    @staticmethod
    async def signup(user_data: UserRequest, db: AsyncSession):
    # 예외 처리 후 jwt_handle.get_password_hash 로  비밀번호 해쉬화
    # 유저 생성
    # UserCrud.new_user 로 db 에 등록
    # 리턴 받은 new_user를 커밋-리프레시 (예외 처리)
        pass

    @staticmethod
    async def login(user:UserRequest,db:AsyncSession):
    # UserCrud.get_by_id 로 해당 유저 가져옴
    # jwt_handle.verify_password 로 해쉬화된 비밀번호 조회 (예외 처리)
    # jwt_handle.create_refresh_token
    # jwt_handle.create_access_token 에 user_id를 넣어 새 토큰 생성
    # 입력한 유저의 리프레시 토큰 업데이트 UserCrud.update_refresh_token_by_id
    # db에 커밋-리프레시
        pass

    @staticmethod
    async def get_user(user_id:int,db:AsyncSession):
        # UserCrud.get_by_id 로 해당 유저 조회(예외처리)
        # 그 유저 그대로 반환
        pass
    @staticmethod
    async def get_all_users(db):
        # UserCrud.get_all(db) 로 유저 리스트 저장(예외처리)
        # 반환
        pass

    @staticmethod
    async def get_user_2(user_id:int,current_user_id:int,db:AsyncSession):
        # current_user_id 가 있는지 확인(예외처리)
        # UserCrud.get_by_id 로 가져오기(예외처리)
        # 그유저그대로 리턴
        pass
    @staticmethod
    async def update_user(user_id:int,userupdate:UserUpdate,db:AsyncSession):
        # user_id 가 있는지 확인 (예외처리)
        # 입력한 비밀번호 해쉬화 get_password_hash
        # UserCrud.update_by_id 로 로그인된 지금 유저 업데이트 후 그정보리턴
        # 리턴된 새 유저에 대한 예외처리
        # 커밋 후 리턴
        pass

    @staticmethod
    async def delete_user(user_id:int,current_user_id:int,db:AsyncSession):
        # current_user_id 가 있는지 확인 (예외처리)(로그인확인)
        # UserCrud.delete_by_id(user_id,db)로 해당 아이디 삭제
        pass

    @staticmethod
    async def dup_check(user_id:int,db:AsyncSession):
        # UserCrud.get_by_id 로 가져오기
        # 만족하는 행이 없으면 사용가능
        # 있으면 중복 을 반환
        pass