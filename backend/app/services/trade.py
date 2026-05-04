from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.db.crud.trade import TradeCrud
from app.db.crud.user import UserCrud
from app.services.balance import BalanceService
from app.services.user import UserService
from app.db.scheme.trade import TradeCreate

class TradeService:
    @staticmethod
    async def my_trade_list(login_id: str, limit: int, offset: int, db: AsyncSession):        
        return await TradeCrud.get_list_by_login_id(login_id, limit, offset, db)

    @staticmethod
    async def new_trade(login_id: str, trade_data: TradeCreate, db: AsyncSession):
        if trade_data.quantity <= 0 or trade_data.price <= 0:
            raise HTTPException(status_code=400, detail="거래 수량 및 가격은 1 이상이어야 합니다.")

        if trade_data.buy_type not in ("buy", "sell"):
            raise HTTPException(status_code=400, detail="buy_type은 'buy' 또는 'sell' 이어야 합니다.")

        try:
            # 1. 유저 조회 (중복된 CRUD 메서드 대신 기존 get_by_login_id 사용)
            user = await UserCrud.get_by_login_id(login_id, db)
            if not user:
                raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

            total_trade_price = trade_data.price * trade_data.quantity

            # 2. 매수 시 현금 검증
            if trade_data.buy_type == "buy" and user.money < total_trade_price:
                raise HTTPException(status_code=400, detail="현금 잔액이 부족하여 매수할 수 없습니다.")

            # 3. 잔고(Balance) 로직 위임 (balance.py가 처리)
            await BalanceService.process_trade_balance(login_id, trade_data, db)

            # 4. 유저 현금(Money) 갱신
            if trade_data.buy_type == "buy":
                user.money -= total_trade_price
            elif trade_data.buy_type == "sell":
                user.money += total_trade_price
            
            # 5. 유저 자산 평가금액 위임 (user.py가 처리)
            await UserService.update_user_valuation(login_id, db)

            # 6. 거래 내역(Trade) 생성
            new_trade = await TradeCrud.create(login_id, trade_data, db)
            
            await db.commit()
            await db.refresh(new_trade)
            
            return new_trade

        except HTTPException as e:
            await db.rollback()
            raise e
            
        except Exception as e:
            await db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=f"거래를 처리하는 중 내부 오류가 발생했습니다: {str(e)}"
            )