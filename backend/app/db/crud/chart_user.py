from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.chart_user import ChartUser
from app.db.scheme.chart_user import ChartuserGet,ChartuserUpdate

class ChartuserCrud:

    @staticmethod
    async def get_by_id_ud(up_date:int,user_id:int,db:AsyncSession):
        # user_id 에 맞는 행을 Chartuser 리스트에서 싹다 반환
        # 리스트를 up_date 내림차순으로 정렬후 10개 뽑아서 반환
        pass

    @staticmethod
    async def new_chartuser(user_id:int,chart:ChartuserUpdate,db:AsyncSession):
        # 입력된 모든 정보를 기반으로 새 chartuser 생성
        # db에 add
        # 그 유저 그대로 리턴
        pass