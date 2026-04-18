from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer,UniqueConstraint
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .news_user import NewsUser
    from .effects import Effects
class News(Base):
    __tablename__ = "news"

    
    news_id: Mapped[int] = mapped_column(primary_key=True)
    news_title: Mapped[str] = mapped_column(String(50),nullable=False)
    news_comments: Mapped[str] = mapped_column(String(50))
    
    news_users: Mapped[list["NewsUser"]] = relationship(back_populates="news", cascade="all, delete-orphan")
    effects: Mapped[list["Effects"]] = relationship(back_populates="news", cascade="all, delete-orphan")