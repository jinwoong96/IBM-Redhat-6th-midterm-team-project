from pydantic import BaseModel,Field, ConfigDict
from .news import NewsRead
from typing import Optional

class NewsUserBase(BaseModel):
    day: int=Field(..., ge=0)
    login_id:str=Field(...,max_length=50)
    news_id:int=Field(...)


class NewsUserRead(BaseModel):#인증된 사용자의 과거 뉴스내역# NewsUserBase 상속했었다가 로그인아이디가 필수인 부분때문에 스웨거에서 에러나서 독립적으로 정의
    # news_user_id: Optional[int] = None #이미 인증된 사용자에게 또 아이디를 보여줄 필요가없음 db필드에 없기도 해서 삭제함
    day: int
    news_id: int
    news_title: str #서비스에서 받은 뉴스제목을 돌려주기위해서
    news_comments: str#내용 또한 같음
    
    model_config = ConfigDict(from_attributes=True)

class NewsuserAdd(NewsUserBase):
    news_user_id:int=Field(None)
    

    model_config = ConfigDict(from_attributes=True)
 
    
    
