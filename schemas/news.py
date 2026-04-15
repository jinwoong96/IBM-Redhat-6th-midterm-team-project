from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class NewsBase(BaseModel):
    news_id: int
