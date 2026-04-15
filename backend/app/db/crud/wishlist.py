from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.wishlist import Wishlist


class WishlistCrud:

    @staticmethod
    async def new_wishlist(item_code:str,user_id:str,db:AsyncSession):
        # Wishlist 라우터에서 받은 정보를 그대로 새 위시리스트 생성
        # db.add , 그 유저 그대로 리턴
        pass

    @staticmethod
    async def get_by_id(user_id:str,db:AsyncSession):
        # 입력한 user_id에 대응되는 모든 튜플을 리스트로 반환
        pass

    @staticmethod
    async def delete_by_id_itemcode(item_code:str,user_id:str,db:AsyncSession):
        # 입력한 종목코드와 아이디를 동시 만족하는 행을 삭제
        # db.delete , flush
        # 삭제 성공시 성공했다는 메세지 리턴
        pass