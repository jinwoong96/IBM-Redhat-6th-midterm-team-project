from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.chart_user import ChartUser
from app.db.crud.chart_init import ChartInitCrud
from app.db.scheme.chart_user import ChartuserUpdate
from sqlalchemy.future import select
from app.db.crud.chart_user import ChartuserCrud
from fastapi import HTTPException, status
from sqlalchemy import func
from app.db.models.item import Item
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token
class ChartuserService:

    @staticmethod
    async def get_chartuser(login_id:str, item_code:str, limit:int, db:AsyncSession):#특정종목 히스토리 조회
        history = await ChartuserCrud.get_by_id_code(login_id, item_code, limit, db)

        if not history:
            raise HTTPException(status_code=404, detail='차트 데이터가 존재하지 않습니다')
        
        return history


    @staticmethod
    async def init_chartuser(login_id:str,db:AsyncSession): #1일차때 원본db 사용자용으로 가져오는 부분
        init_data=await ChartInitCrud.get_first_data(db)
        if not init_data:
            raise HTTPException(status_code=500,detail='관리자에게 문의하세요')
        
        try:
            for i in init_data:
                chart_data = ChartuserUpdate(
                    item_code=i.item_code,
                    start_price=i.start_price,
                    end_price=i.end_price,
                    max_price=i.max_price,
                    min_price=i.min_price,
                    day=i.day,
                    flu_range=i.flu_range,
                    flu_range_percent=i.flu_range_percent
                )
                await ChartuserCrud.create_all(user_id=login_id,chart=chart_data,db=db)

            await db.commit()
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500,detail='초기화 실패 오류발생')
        
        return True

    @staticmethod
    async def get_itemlist(login_id:str, db:AsyncSession):#현재 진행일차의 모든 종목 목록 조회
        day_data=select(func.max(ChartUser.day)).filter(ChartUser.login_id==login_id)#인증된 사용자의 가장 최신날짜 선택
        day_result=await db.execute(day_data)
        current_day= day_result.scalar()

        if current_day is None:
            raise HTTPException(status_code=404,detail='현재 데이터가 없습니다')
        
        query=(
            select(
                Item.item_code,      # 종목테이블이랑 조인
                Item.item_name,      
                Item.category_name,  
                ChartUser.flu_range_percent,
                ChartUser.end_price
            )
            .join(Item,ChartUser.item_code==Item.item_code).filter(ChartUser.login_id==login_id,ChartUser.day==current_day)
        )

        result = await db.execute(query)
        return result.mappings().all()