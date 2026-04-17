from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Annotated

class WishListCreate(BaseModel):
    login_id: str  
    item_code: str