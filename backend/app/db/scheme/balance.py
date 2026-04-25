from pydantic import BaseModel, Field, ConfigDict

class BalanceResponse(BaseModel):
    item_code : str =Field(...,description="종목 이름")
    item_name: str = Field(..., description="종목명")
    quantity: int = Field(..., description="보유 수량")
    purchase_price: int = Field(..., description="총 구매가 (수량 * 매입단가)")
    val_price: int = Field(..., description="평가금액 (수량 * 현재가)")
    val_profit_and_loss: int = Field(..., description="평가손익")
    rate_of_return: float = Field(..., description="수익률 (%)")

    model_config = ConfigDict(from_attributes=True)