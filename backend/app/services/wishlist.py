from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.trade import Trade
from sqlalchemy.future import select
from app.db.crud.wishlist import WishlistCrud
from fastapi import HTTPException, status
from app.core.jwt_handle import get_password_hash, verify_password, create_access_token,create_refresh_token

class WishlistService:

    @staticmethod
    async def add_wishlist(login_id: str, item_code: str, db: AsyncSession):
       
        existing_wish = await WishlistCrud.get_by_user_and_item(login_id, item_code, db)
        if existing_wish:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="이미 관심 종목에 추가되어 있습니다."
            )
        new_wish = await WishlistCrud.create(login_id, item_code, db)
        await db.commit()
        await db.refresh(new_wish)
        return new_wish

    @staticmethod
    async def user_wishlist(login_id: str, db: AsyncSession):
        return await WishlistCrud.get_all_by_login_id(login_id, db)
    
    @staticmethod
    async def delete_wishlist(login_id: str, item_code: str, db: AsyncSession):
        existing_wish = await WishlistCrud.get_by_user_and_item(login_id, item_code, db)
        if not existing_wish:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="관심 종목을 찾을 수 없습니다."
            )

        await WishlistCrud.delete(existing_wish, db)
        await db.commit()
        return existing_wish