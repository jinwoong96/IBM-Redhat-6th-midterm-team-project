from pydantic import BaseModel,Field





class UserCreate(BaseModel):
# 사용자 생성 시 필요한 정보
    pass

class UserLogin(BaseModel):
# 로그인 시 필요한 정보
    pass


class UserUpdate(BaseModel):
# 유저 정보 업데이트시 사용
# None 값 허용 기본 값 None
    pass