from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[str] = mapped_column(String(50),primary_key=True)
    user_nickname: Mapped[str] = mapped_column(String(50),nullable=False, unique=True)
    user_password: Mapped[str] = mapped_column(String(50),nullable=False)
    money: Mapped[int] = mapped_column(Integer,CheckConstraint("money >= 0"),default=50000000)
    valuation: Mapped[int] = mapped_column(Integer,CheckConstraint("valuation >= 0"),default=0)
    created_at: Mapped[datetime]= mapped_column(TIMESTAMP, server_default=func.now())
    refresh_token: Mapped[Optional[str]]=mapped_column(String(255), nullable=True)