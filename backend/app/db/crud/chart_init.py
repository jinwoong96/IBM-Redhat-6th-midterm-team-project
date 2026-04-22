from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.chart_init import ChartInit


class ChartInitCrud:

    @staticmethod
    async def get_all(db:AsyncSession):#원본데이터 전체
        query=select(ChartInit)
        result=await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def get_first_data(db:AsyncSession):#1일차에서 쓰일 원본데이터
        query=select(ChartInit).filter(ChartInit.day==1)
        result=await db.execute(query)
        return result.scalars().all()