from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class BalanceBase(BaseModel):
    user_id:int

class BalanceResponse(BalanceBase):
    item_code:str
    quantity:int
    purchase_pric:int
    val_price:int
    val_profit_and_loss:int
    rate_of_return:float

    model_config = ConfigDict(from_attributes=True)