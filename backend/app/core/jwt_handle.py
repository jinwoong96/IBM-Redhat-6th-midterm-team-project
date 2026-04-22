from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.core.settings import settings
import uuid
import jwt

pw_crypt=CryptContext(schemes=['bcrypt'])

def get_password_hash(password:str):
    # 해쉬화 후 리턴
    trunc_pw=password.encode('utf-8')[:72]
    return pw_crypt.hash(trunc_pw)


def verify_password(plain_pw:str, hashed_pw:str):
    # 비밀번호 검증
    trunc_pw=plain_pw.encode('utf-8')[:72]
    return pw_crypt.verify(trunc_pw, hashed_pw)


def create_token(login_id:str, expires_seconds:int, **kwargs):
    # 기본 토큰 생성 함수 jwt.encode
    expire=datetime.now(timezone.utc)+timedelta(seconds=expires_seconds)
    
    to_encode=kwargs.copy()
    to_encode.update({'exp':expire, 'login_id':login_id})

    return jwt.encode(to_encode, settings.secret_key, settings.jwt_algorithm)
    

def create_access_token(login_id:str):
    # 액세스 토큰
    return create_token(login_id=login_id, expires_seconds=settings.access_token_expire_seconds)


def create_refresh_token(login_id:str):
    # 리프레시 토큰
    return create_token(login_id=login_id, jti=str(uuid.uuid4()),expires_seconds=settings.refresh_token_expire_seconds)

# 토큰 디코딩-> payload dict 반환 (검증: 변조 여부 확인)
def decode_token(token:str):
    return jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])

# 토큰 디코딩-> uid값 불러오기
def verify_token(token:str):
    payload=decode_token(token)
    return payload.get('login_id')