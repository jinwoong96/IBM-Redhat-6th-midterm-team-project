from pydantic import BaseModel,Field,ConfigDict



class BalanceUpdate(BaseModel):
    item_code:str
    quantity:int
    purchase_price:int
    val_price:int | None = Field(default=None,description="평가금액")
    val_profit_and_loss:int | None = Field(default=None,description="평가손익")
    rate_of_return:float | None = Field(default=None,description="수익률")
    
    model_config = ConfigDict(from_attributes=True)
    # 잔고의 모든 정보
    # 평가금액, 평가손익, 수익률 은 none 값이여도되게 설정 기본값 none
    