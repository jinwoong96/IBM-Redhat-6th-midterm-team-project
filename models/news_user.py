from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
from user import User
from news import News
class NewsUser(Base):
    __tablename__ = "news_users"
    news_user_id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(Integer, CheckConstraint("day >= 0"),nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.user_id"),nullable=False)
    news_id: Mapped[int] = mapped_column(ForeignKey("news.news_id"),nullable=False)
    
    user:Mapped["User"]=relationship(back_populates="newsuser")
    news:Mapped["News"]=relationship(back_populates="newsuser")