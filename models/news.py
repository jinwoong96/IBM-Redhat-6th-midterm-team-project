from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

class News(Base):
    __tablename__ = "news"
    news_id: Mapped[int] = mapped_column(primary_key=True)
    news_title: Mapped[str] = mapped_column(String(20),nullable=False)
    news_comments: Mapped[str] = mapped_column(String(50))