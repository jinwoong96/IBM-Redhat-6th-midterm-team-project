from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

class Ranking(Base):
    __tablename__ = "rankings"
    ranking_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id",ondelete="CASCADE"))
    max_accounts: Mapped[int] = mapped_column(Integer,nullable=False)
    max_plus: Mapped[float] = mapped_column(Float,nullable=False)
    day:  Mapped[int] = mapped_column(Integer,nullable=False)
    