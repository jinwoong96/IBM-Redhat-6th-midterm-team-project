from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.wishlist import WishlistService
from app.core.auth import get_current_user

router = APIRouter(prefix="/wishlist", tags=["wishlist"])

@router.post("/{item_code}",)
async def add_wishlist(item_code:str,current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # WishlistService.add_wishlist 실행
    pass



@router.get("/{user_id}",)
async def user_wishlist(user_id:str,current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # WishlistService.user_wishlist(user_id,current_user_id,db) 실행
    pass


@router.delete("/{item_code}",)
async def delete_wishlist(item_code:str,current_user=Depends(get_current_user),
             db:AsyncSession=Depends(get_db)):
    # WishlistService.delete_wishlist 실행
    pass