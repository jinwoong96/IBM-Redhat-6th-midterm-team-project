from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class TradeBase(BaseModel):
    trade_id:int

class TradeCreate(BaseModel):
    item_code:str
    buy_type:str
    price:int
    quantity:int

class TradeResponse(TradeBase):
    item_code:str
    buy_type:str
    price:int
    quantity:int
    trade_day:int
    user_id:int

    model_config = ConfigDict(from_attributes=True)