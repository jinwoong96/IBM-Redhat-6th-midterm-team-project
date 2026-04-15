from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.chart_user import ChartUser
from app.db.scheme.chart_user import ChartuserGet,ChartuserUpdate

class ChartuserCrud:

    @staticmethod
    async def get_by_id_ud(up_date:int,user_id:str,db:AsyncSession):
        # user_id 에 맞는 행을 Chartuser 리스트에서 싹다 반환
        # 리스트를 up_date 내림차순으로 정렬후 10개 뽑아서 반환
        # 만약 표시하려는 차트 데이터 행이 부족하면, chart_init 을 내림차순으로 
        # 정렬하고 위에서부터 부족한만큼 가져와서 10개를 채움
        pass

    @staticmethod
    async def new_chartuser(user_id:str,chart:ChartuserUpdate,db:AsyncSession):
        # 입력된 모든 정보를 기반으로 새 chartuser 생성
        # db에 add
        # 그 유저 그대로 리턴
        pass