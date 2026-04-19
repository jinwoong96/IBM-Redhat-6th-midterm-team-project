from pydantic import BaseModel,Field, ConfigDict


class TradeCreate(BaseModel):
    item_code: str = Field(..., description="거래할 종목 코드")
    buy_type: str = Field(..., description="매수('buy') 또는 매도('sell')")
    price: int = Field(..., ge=0, description="1주당 체결 가격 (0 이상)")
    quantity: int = Field(..., ge=0, description="체결 수량 (0 이상)")

class TradeResponse(BaseModel):
    trade_id: int
    login_id: str
    item_code: str
    buy_type: str
    price: int
    quantity: int
    trade_day: int

    model_config = ConfigDict(from_attributes=True)