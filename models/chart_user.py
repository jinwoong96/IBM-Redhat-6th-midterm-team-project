from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

class Chart_user(Base):
    __tablename__ = "chart_users"

    chart_user_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id",ondelete="CASCADE"),Integer)
    item_code: Mapped[str] = mapped_column(ForeignKey("items.item_code"),index=True)
    start_price: Mapped[int] = mapped_column(Integer,CheckConstraint("start_price >= 0"))
    end_price: Mapped[int] = mapped_column(Integer,CheckConstraint("end_price >= 0"))
    max_price: Mapped[int] = mapped_column(Integer,CheckConstraint("max_price >= 0"))
    min_price: Mapped[int] = mapped_column(Integer,CheckConstraint("min_price >= 0"))
    day:  Mapped[int] = mapped_column(Integer)
    거래_체결: 