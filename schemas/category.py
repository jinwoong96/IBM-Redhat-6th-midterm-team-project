from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    category_id: int
    
