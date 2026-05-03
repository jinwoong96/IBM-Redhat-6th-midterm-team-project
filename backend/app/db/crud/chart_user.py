from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.scheme.chart_user import ChartuserCreate
from app.db.models.chart_user import ChartUser
from sqlalchemy import desc, func, delete
from fastapi import HTTPException
from app.db.models.item import Item

class ChartuserCrud:

    @staticmethod
    async def get_by_id_code(user_id:str, item_code:str, limit:int, db:AsyncSession):#명세서 8번 인증된사용자의 특정종목 차트히스토리 조회 
        query=(
            select(ChartUser).filter(ChartUser.login_id==user_id,ChartUser.item_code==item_code).order_by(desc(ChartUser.day)).offset(1).limit(limit)
        )
        result=await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def create_all(user_id:str,chart:ChartuserCreate,db:AsyncSession): #사용자 차트생성
        new_chart=ChartUser(login_id=user_id,**chart.model_dump())

        db.add(new_chart)
        return new_chart
    
    @staticmethod
    async def is_exist(login_id:str, db:AsyncSession):
        day_data=select(func.max(ChartUser.day)).filter(ChartUser.login_id==login_id)#인증된 사용자의 가장 최신날짜 선택
        day_result=await db.execute(day_data)
        current_day= day_result.scalar()

        if current_day is None:
            return False
        else:
            return True
    

    @staticmethod
    async def get_item_list_crud(login_id:str, day_offset:int, db:AsyncSession):
        day_data=select(func.max(ChartUser.day)).filter(ChartUser.login_id==login_id)#인증된 사용자의 가장 최신날짜 선택
        day_result=await db.execute(day_data)
        next_day= day_result.scalar()

        if next_day is None:
            return None
        
        query=(
            select(
                Item.item_code,      # 종목테이블이랑 조인
                Item.item_name,      
                Item.category_name,  
                ChartUser.flu_range_percent,
                ChartUser.end_price
            )
            .join(Item,ChartUser.item_code==Item.item_code).filter(ChartUser.login_id==login_id,ChartUser.day==next_day-day_offset)
        )
        result = await db.execute(query)
        return result.mappings().all()
    
    @staticmethod #아이템코드로 아이템이름뽑아오는 거
    async def get_name_by_code(item_code: str, db: AsyncSession):
    
        item_data= select(Item.item_code, Item.item_name).filter(Item.item_code == item_code)
    
        result = await db.execute(item_data)
        return result.mappings().first()
    
    @staticmethod
    async def get_last_day_by_user(login_id: str, db: AsyncSession):
        result = await db.execute(
            select(ChartUser.day)
            .filter(ChartUser.login_id == login_id)
            .order_by(ChartUser.day.desc())
            .limit(1)
        )
        return result.scalar()
    
    @staticmethod
    async def delete_old_data(login_id: str, max_day: int, db: AsyncSession):
        stmt = delete(ChartUser).where(
            ChartUser.login_id == login_id,
            ChartUser.day <= max_day
        )

        await db.execute(stmt)