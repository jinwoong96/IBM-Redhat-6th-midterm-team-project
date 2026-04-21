from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
class Ranking(Base):
    __tablename__ = "rankings"
    ranking_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    max_accounts: Mapped[int] = mapped_column(Integer,CheckConstraint("max_accounts >= 0"),nullable=False)
    max_plus: Mapped[float] = mapped_column(Float,nullable=False)
    day:  Mapped[int] = mapped_column(Integer,CheckConstraint("day >= 0"),nullable=False)
    login_id: Mapped[str] = mapped_column(String(50),ForeignKey("users.login_id",ondelete="CASCADE"),unique=True)
    
    user:Mapped["User"]=relationship(back_populates="ranking")
    
