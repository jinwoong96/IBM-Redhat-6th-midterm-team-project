from pydantic import BaseModel, ConfigDict, Field

class ChartInitBase(BaseModel):
    item_code: str = Field(..., max_length=10)
    start_price: int = Field(..., ge=0)
    end_price: int = Field(..., ge=0)
    max_price: int = Field(..., ge=0)
    min_price: int = Field(..., ge=0)
    flu_range: int
    flu_range_percent: float
    day: int = Field(..., ge=0)

class ChartInitRead(ChartInitBase):#맨처음 만들때에는 차트아이디가 아직없으므로 베이스에서는 뺀다.
    chart_id: int

    model_config=ConfigDict(from_attributes=True)