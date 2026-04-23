from pydantic import BaseModel, Field
from typing import Annotated, Optional
from datetime import datetime


class UserCreate(BaseModel):
# 사용자 생성 시 필요한 정보
    login_id:str=Field(...)
    user_nickname:str=Field(..., max_length=50)
    user_password:Annotated[str,Field(..., max_length=255)]

class UserInfo(BaseModel):
    login_id: str
    user_nickname: str
    money: int
    valuation: int
    created_at: datetime

    class Config:
        from_attributes=True

class UserLogin(BaseModel):
# 로그인 시 필요한 정보
    login_id:str=Field(...)
    user_password:Annotated[str,Field(..., max_length=255)]

class TokenResponse(BaseModel):
    access_token:str
    token_type:str='bearer'
    user: UserInfo

class UserUpdate(BaseModel):
# 유저 정보 업데이트시 사용
# None 값 허용 기본 값 None
    user_nickname:Optional[str]=Field(None, max_length=50)
    
    old_password:Optional[str]=Field(None, min_length=8, max_length=255)
    new_password:Optional[str]=Field(None, min_length=8, max_length=255)