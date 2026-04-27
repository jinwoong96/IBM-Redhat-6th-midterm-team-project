from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.progress import ProgressService
from app.core.auth import get_current_user
from app.services.news_user import NewsuserService

router = APIRouter(prefix="/progress", tags=["progress"])


@router.put("/next_turn")
async def turn(current_user=Depends(get_current_user),
                     db: AsyncSession = Depends(get_db)):
    res=await ProgressService.turn(login_id=current_user, db=db)
    await NewsuserService.add_newsuser(
        login_id=current_user,
        db=db
    )

    return res