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

               
        return history


    @staticmethod
    async def init_chartuser(login_id:str,db:AsyncSession): #1일차때 원본db 사용자용으로 가져오는 부분
        
        existing = await ChartuserCrud.get_item_list_crud(login_id, db)
        if existing:
            return True # init 데이터 중복 확인
        
        init_data=await ChartInitCrud.get_first_data(db)
        if not init_data:
            raise HTTPException(status_code=500,detail='초기 데이터 불러오기 오류')
        
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
            print(e)
            await db.rollback()
            raise HTTPException(status_code=500,detail='초기화 실패 오류발생')
        
        return True

    @staticmethod
    async def get_itemlist(login_id:str, db:AsyncSession):#현재 진행일차의 모든 종목 목록 조회
        items=await ChartuserCrud.get_item_list_crud(login_id,db)
        
                
        return items
        #조인 쿼리문 crud로 옮김
    
     
    
    @staticmethod#코드로 아이템이름뽑아오는 거
    async def get_item_name(item_code: str, db: AsyncSession):
  
        item = await ChartuserCrud.get_name_by_code(item_code, db)

        return item      