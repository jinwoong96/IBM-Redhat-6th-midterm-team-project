from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.wishlist import WishlistCrud

class WishlistService:

    @staticmethod
    async def add_wishlist(login_id: str, item_code: str, db: AsyncSession):
        #  이미 추가된 관심 종목인지 확인
        existing_wish = await WishlistCrud.get_by_user_and_item(login_id, item_code, db)
        if existing_wish:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="이미 관심 종목에 추가되어 있습니다."
            )
           
        try:
            #  관심 종목 생성 및 커밋
            new_wish = await WishlistCrud.create(login_id, item_code, db)
            await db.commit()
            await db.refresh(new_wish)
            return new_wish         
        except Exception as e:
            # 에러 발생 시 롤백 (DB 꼬임 방지)
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    async def user_wishlist(login_id: str, db: AsyncSession):
        # 관심 종목 목록 조회
        return await WishlistCrud.get_all_by_login_id(login_id, db)
    
    @staticmethod
    async def delete_wishlist(login_id: str, item_code: str, db: AsyncSession):
        existing_wish = await WishlistCrud.get_by_user_and_item(login_id, item_code, db)
        if not existing_wish:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="관심 종목을 찾을 수 없습니다."
            )

        try:
            await WishlistCrud.delete(existing_wish, db)
            await db.commit()
            return existing_wish # 라우터에서 Response Model로 반환하기 위해 리턴
            
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))