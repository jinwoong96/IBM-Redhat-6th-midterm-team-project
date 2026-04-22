from pydantic import BaseModel

# 업데이트 및 내 정보
class RankingResponse(BaseModel):
    login_id: str
    user_nickname: str
    max_accounts: int
    max_plus: float
    day: int
    rank: int

    class Config:
        from_attributes = True

# TOP 10 
class Top10Response(BaseModel):
    rank: int
    login_id: str
    user_nickname: str
    max_accounts: int

    class Config:
        from_attributes = True