from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone
from typing import Annotated

class WishListCreate(BaseModel):
    login_id: str  
    item_code: str

class WishlistResponse(BaseModel):
    wishlist_id: int
    login_id: str
    item_code: str

    model_config = ConfigDict(from_attributes=True)