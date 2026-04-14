from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class RankingBase(BaseModel):
    ranking_id : int

class RankingCreate(BaseModel):
    max_accounts: int
    max_plus: float
    day: int

class RankingResponse(RankingBase):
    max_accounts: int
    max_plus: float
    day: int
    user_id:int
    
    model_config = ConfigDict(from_attributes=True)