from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List

class NewsBase(BaseModel):
    news_title: str=Field(...,max_length=50)
    news_comments: str=Field(...,max_length=50)

class NewsRead(NewsBase):
    news_id: int
    model_config = ConfigDict(from_attributes=True)