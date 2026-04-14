from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class ChartUserBase(BaseModel):
    chart_user_id:int

class ChartUserUpdate(BaseModel):
    item_code:str
    start_price:int
    end_price:int
    max_price:int
    min_price :int

class ChartUserResponse(ChartUserBase):
    # relationship필요할듯?