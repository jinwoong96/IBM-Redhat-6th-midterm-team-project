from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer, UniqueConstraint
from typing import Optional, List, TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User
    from .news import News
class NewsUser(Base):
    __tablename__ = "news_users"

    __table_args__ = (
        UniqueConstraint('login_id', 'day', 'news_id', name='uq_news_users_login_day_news'),
    )
    news_user_id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(Integer, CheckConstraint("day >= 0"),nullable=False)
    login_id: Mapped[str] = mapped_column(String(50),ForeignKey("users.login_id", ondelete="CASCADE"),nullable=False)
    news_id: Mapped[int] = mapped_column(Integer,ForeignKey("news.news_id"),nullable=False)
    
    user:Mapped["User"]=relationship(back_populates="news_users")
    news:Mapped["News"]=relationship(back_populates="news_users")