from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.balance import BalanceCrud

class BalanceService:
    @staticmethod
    async def my_balance(login_id: str, db: AsyncSession):
        try:
            # 잔고 내역 조회 (잔고가 없으면 빈 리스트 [] 반환)
            balances = await BalanceCrud.get_by_id(login_id, db)
            return balances
            
        except Exception:
            # 의도치 않은 파이썬/DB 내부 에러 방어
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="잔고 내역을 불러오는 중 서버에 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
            )