from pydantic import BaseModel,Field,ConfigDict
from .chart_init import ChartInitBase



class ChartuserGet(BaseModel):
    # 유저 아이디와 종목코드 
    chart_user_id: int
    item_code: str = Field(..., max_length=10)


class ChartuserUpdate(ChartInitBase):
    # item_code,start_price, end_price, max_price, min_price, day, flu_range, flu_range_percent
    pass

class ChartuserRead(ChartuserUpdate):#db에 왓다갓다거릴 전체필드
    chart_user_id: int
    login_id: str

    model_config = ConfigDict(from_attributes=True)