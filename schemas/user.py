from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

# 1. 공통 Base 스키마 (모든 User 스키마의 뼈대)
class UserBase(BaseModel):
    user_nickname: str = Field(max_length=50)

# 2. 회원가입 요청 스키마 (POST /users)
class UserCreate(UserBase):
    user_password: str = Field(max_length=50)  # 생성 시에는 비밀번호가 필수

# 3. 회원정보 수정 요청 스키마 (PUT /users)
class UserUpdate(BaseModel):
    user_nickname: Optional[str] = Field(None,max_length=50)
    user_password: Optional[str] = Field(None,max_length=50)

# 4. 클라이언트에게 반환할 응답 스키마 (GET /users, GET /users/{user_id} 등)
class UserResponse(UserBase):
    user_id: str
    money: int
    valuation: int
    created_at: datetime
    
    # SQLAlchemy 모델 객체를 Pydantic 모델로 자동 변환하도록 허용 (Pydantic V2 문법)
    model_config = ConfigDict(from_attributes=True)

