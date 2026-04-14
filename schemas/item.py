from pydantic import BaseModel, ConfigDict , Field
from typing import Optional
from datetime import datetime
# 1. 공통 Base 스키마
class ItemBase(BaseModel):
    item_code: str
    item_name: str
    category_id: int
    curr_price: int
    
    # 모델에서 nullable=False가 없으므로 Null(None)이 들어올 수 있음
    flu_range: Optional[int] = None
    flu_range_percent: Optional[float] = None

# 2. 조회 응답용 스키마 (GET)
class ItemResponse(ItemBase):
    # SQLAlchemy 모델 객체를 Pydantic 모델로 변환 허용
    model_config = ConfigDict(from_attributes=True)
    