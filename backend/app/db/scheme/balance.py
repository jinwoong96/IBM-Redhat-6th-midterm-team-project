from pydantic import BaseModel,Field



class BalanceUpdate(BaseModel):
    # 잔고의 모든 정보
    # 평가금액, 평가손익, 수익률 은 none 값이여도되게 설정 기본값 none
    pass