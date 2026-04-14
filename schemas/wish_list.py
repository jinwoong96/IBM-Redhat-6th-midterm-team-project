from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime

class WishlistBase(BaseModel):
    wishlist_id: int


class WishlistResponse(WishlistBase):
       user_id:str
       item_code:str
       model_config = ConfigDict(from_attributes=True)
    