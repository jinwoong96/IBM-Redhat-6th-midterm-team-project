from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.balance import Balance
from app.db.scheme.balance import BalanceUpdate


class BalanceCrud:

    @staticmethod
    async def get_last_trade(user_id:int,db:AsyncSession):
        # user_id 에 맞는 행 중 가장 최신에 생긴 행을 추출
        # 그 행을 리턴
        pass


    @staticmethod
    async def update_my_balance(balance:BalanceUpdate,db:AsyncSession):

        # 입력된 정보를 바탕으로 정보 업데이트
        # 만약 구매 타입이 판매이면 db.delete  (리턴 :삭제 했다는 메세지)
        # 만약 이미 있는 종목이고 구매 타입이 구입이면 그 행을 꺼내 값을 대입
        # 만약 없는 종목이고 구매 타입이 구입이면 새 balance를 만들어 db.add
        # 구매타입이면 (리턴 : 업뎃된 잔고)
        pass

    @staticmethod
    async def get_by_id(user_id:int,db:AsyncSession):
        # user_id 에 맞는 모든 행을 리스트로 출력
        # 반환
        pass