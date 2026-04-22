from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.scheme.chart_user import ChartuserUpdate
from app.db.models.chart_user import ChartUser
from sqlalchemy import desc
from sqlalchemy import func
from fastapi import HTTPException
from app.db.models.item import Item

class ChartuserCrud:

    @staticmethod
    async def get_by_id_code(user_id:str, item_code:str, limit:int, db:AsyncSession):#명세서 8번 인증된사용자의 특정종목 차트히스토리 조회 
        query=(
            select(ChartUser).filter(ChartUser.login_id==user_id,ChartUser.item_code==item_code).order_by(desc(ChartUser.day)).limit(limit)
        )
        result=await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def create_all(user_id:str,chart:ChartuserUpdate,db:AsyncSession): #사용자 차트생성
        new_chart=ChartUser(login_id=user_id,**chart.model_dump())

        db.add(new_chart)
        return new_chart
    
    @staticmethod
    async def get_item_list_crud(login_id:str, db:AsyncSession):
        day_data=select(func.max(ChartUser.day)).filter(ChartUser.login_id==login_id)#인증된 사용자의 가장 최신날짜 선택
        day_result=await db.execute(day_data)
        current_day= day_result.scalar()

        if current_day is None:
            return None
        
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