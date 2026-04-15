from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class NewsUserBase(BaseModel):
    news_user_id: int

class NewsUserCreate(NewsUserBase):
    news_id: int
    day: int

class NewsUserResponse(NewsUserBase):
    day: int
    user_id: int
    news_id: int