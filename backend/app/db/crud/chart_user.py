from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.scheme.chart_user import ChartuserUpdate
from app.db.models.chart_user import ChartUser
from sqlalchemy import desc

class ChartuserCrud:

    @staticmethod
    async def get_by_id_code(user_id:str, item_code:str, limit:int, db:AsyncSession):#명세서 8번 인증된사용자의 특정종목 차트히스토리 조회 
        query=(
            select(ChartUser).filter(ChartUser.login_id==user_id,ChartUser.item_code==item_code).order_by(desc(ChartUser.day)).limit(limit)
        )
        result=await db.execute(query)
        return result.scalar().all()

    @staticmethod
    async def create_all(user_id:str,chart:ChartuserUpdate,db:AsyncSession): #사용자 차트생성
        new_chart=ChartUser(login_id=user_id,**chart.model_dump())

        db.add(new_chart)
        return new_chart