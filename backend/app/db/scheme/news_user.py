from pydantic import BaseModel,Field, ConfigDict
from .news import NewsRead


class NewsUserBase(BaseModel):
    day: int=Field(..., ge=0)
    login_id:str=Field(...,max_length=50)
    news_id:int=Field(...)


class NewsUserRead(NewsUserBase):#인증된 사용자의 과거 뉴스내역
    news_user_id: int
        
    model_config = ConfigDict(from_attributes=True)

class NewsuserAdd(NewsUserBase):
    news_user_id:int=Field(None)
    

    model_config = ConfigDict(from_attributes=True)
 
    
    
