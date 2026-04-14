from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.core.settings import settings
import jwt



def get_password_hash(password:str):
    # 해쉬화 후 리턴


def verify_password(plain_pw:str, hashed_pw:str):
    # 비밀번호 검증




def create_token(user_id:int,expires_delta:timedelta,**kwargs):
    # 기본 토큰 생성 함수 jwt.encode


def create_access_token(user_id:int):
    # 액세스 토큰

def create_refresh_token(user_id:int):
    # 리프레시 토큰