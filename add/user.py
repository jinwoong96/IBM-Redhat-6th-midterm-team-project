from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, Integer
from typing import Optional, List, TYPE_CHECKING


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[str] = mapped_column(String(50),primary_key=True, nullable=False)
    user_nickname:  Mapped[str] = mapped_column(String(50),nullable=False)
    user_password: Mapped[str] = mapped_column(String(50), nullable=False)
    money: Mapped[int] = mapped_column(Integer, default=50000000, nullable=False)
    valuation: Mapped[int] = mapped_column(Integer,default=0)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    refresh_token: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    