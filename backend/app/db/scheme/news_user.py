from pydantic import BaseModel,Field, ConfigDict
from .news import NewsRead


class NewsUserBase(BaseModel):
    day: int=Field(..., ge=0)
    login_id:str=Field(...,max_length=50)
    news_id:int=Field(...)

#이거 지난 뉴스기록도 사용자에게 보여주기로한건지 기억이 가물가물해서 일단 주석 보여주는게 좋을거같긴한디
# class NewsUserRead(NewsUserBase):
#     news_user_id: int
#     day: int
#     login_id: str
#     news: NewsRead
    
#     model_config = ConfigDict(from_attributes=True)

class NewsuserAdd(NewsUserBase):
    news_user_id:int=Field(None)
    

    model_config = ConfigDict(from_attributes=True)
 
    
    
