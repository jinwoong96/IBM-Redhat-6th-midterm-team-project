from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, List
from app.db.database import get_db
from app.services.wishlist import WishlistService
from app.core.auth import get_current_user
from app.db.scheme.wishlist import WishlistResponse,WishlistItemResponse

router = APIRouter(prefix="/wishlist", tags=["wishlist"])

@router.post("/items/{item_code}", response_model=WishlistResponse)
async def add_wishlist(
    item_code: Annotated[str, Path(...)],
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    login_id = current_user
    return await WishlistService.add_wishlist(login_id, item_code, db)


@router.get("", response_model=List[WishlistItemResponse])
async def user_wishlist(
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    login_id = current_user
    return await WishlistService.user_wishlist(login_id, db)


@router.delete("/items/{item_code}", response_model=WishlistResponse)
async def delete_wishlist(
    item_code: Annotated[str, Path(...)],
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    login_id = current_user
    return await WishlistService.delete_wishlist(login_id, item_code, db)