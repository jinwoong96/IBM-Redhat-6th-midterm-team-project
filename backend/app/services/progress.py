from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud.user import UserCrud
from app.db.crud.chart_user import ChartuserCrud
from app.db.crud.balance import BalanceCrud
from app.db.crud.ranking import RankingCrud
from fastapi import HTTPException, status
# import traceback # 에러 추적용
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

INIT_ASSET = 50000000

class ProgressService:

    @staticmethod
    async def get_settlement(login_id: str, db: AsyncSession):
        # 1. 유저
        user = await UserCrud.get_user_by_login_id(login_id, db)
        if not user:
            raise HTTPException(status_code=404, detail="유저를 찾을 수 없습니다")

        # 2. 날짜 
        next_day = await ChartuserCrud.get_last_day_by_user(login_id, db)
        if next_day is None:
            raise HTTPException(status_code=400, detail="차트를 찾을 수 없습니다")

        # 3. 데이터 조회
        balance_data = await BalanceCrud.get_by_id(login_id, db)
            
        user_cash = user.money
        total_valuation = user.valuation
        total_asset = user.money + user.valuation
        total_profit_val = total_asset - INIT_ASSET
        total_profit_rate = total_profit_val/INIT_ASSET*100

        response = {
            "today_asset": total_asset,
            "cash": user_cash,
            "valuation": total_valuation,
            "profit": total_profit_val,
            "profit_rate": total_profit_rate,
            "jongmok": balance_data,
            "day" : next_day
        }

        return response

    @staticmethod
    async def turn(login_id: str, db: AsyncSession):
        # 1. 유저
        user = await UserCrud.get_user_by_login_id(login_id, db)
        if not user:
            raise HTTPException(status_code=404, detail="유저를 찾을 수 없습니다")

        # 2. 날짜 
        next_day = await ChartuserCrud.get_last_day_by_user(login_id, db)
        if next_day is None:
            raise HTTPException(status_code=400, detail="차트를 찾을 수 없습니다")

        # 3. 데이터 조회
        balance_data = await BalanceCrud.get_balance_with_prices(login_id, next_day, db)
            
        total_valuation = 0
        jongmok_list = []

        # 4. 정산 계산
        for row in balance_data:
            balance_obj = row[0]
            current_price = row[1]
            item_name = row[2]

            balance_queantity = balance_obj.quantity
            purchase_price = balance_obj.purchase_price
                    
            val_price = float(current_price * balance_queantity)
            buy_total = float(purchase_price)
            p_profit = val_price - buy_total
            p_rate = (p_profit / buy_total * 100) if buy_total != 0 else 0

            balance_obj.val_price = val_price
            balance_obj.val_profit_and_loss = p_profit
            balance_obj.rate_of_return = p_rate
                    
            total_valuation += val_price

            jongmok_list.append({
                "item_code": balance_obj.item_code,
                "item_name": item_name,
                "quantity": balance_queantity,
                "purchase_price": purchase_price,
                "current_price": current_price,
                "valuation": val_price,
                "profit": p_profit,
                "rate": p_rate,
            })

        # 5. 자산 업데이트
        user_cash = user.money
        user.valuation = total_valuation
        total_asset = float((user.money) + total_valuation)
        
        # 6. 랭킹/수익 계산
        total_profit_val = total_asset - INIT_ASSET
        total_profit_rate = (total_profit_val / INIT_ASSET * 100) if INIT_ASSET != 0 else 0
        
        # 7. 랭킹 DB 반영 (인자 순서 db, login_id 순서 확인!)
        my_ranking = await RankingCrud.get_by_login_id(login_id, db)
        if not my_ranking:
            try:
                await RankingCrud.create(login_id=login_id,
                                max_accounts=total_asset,
                                max_plus=total_profit_rate,
                                day=next_day,
                                db=db)
            except:
                raise HTTPException(status_code=500, detail="랭킹 등록에 실패했습니다")
        elif total_asset > my_ranking.max_accounts:
            my_ranking.max_accounts = total_asset
            my_ranking.max_plus = total_profit_rate
            my_ranking.day = next_day

        # 8. 최종 커밋
        await db.commit()

        response = {
            "today_asset": total_asset,
            "cash": user_cash,
            "valuation": total_valuation,
            "profit": total_profit_val,
            "profit_rate": total_profit_rate,
            "jongmok": jongmok_list,
            "day" : next_day
        }

        return True
        # return response