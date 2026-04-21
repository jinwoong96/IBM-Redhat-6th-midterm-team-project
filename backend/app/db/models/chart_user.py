from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer,UniqueConstraint, Index
from typing import Optional, List, TYPE_CHECKING
from .user import User
from .item import Item
class ChartUser(Base):
    __tablename__ = "chart_users"

    __table_args__ = (
        UniqueConstraint('login_id', 'item_code', 'day', name='uix_chart_users_login_id_item_code_day'),
    
        Index('idx_chart_users_login_item_day', 'login_id', 'item_code', 'day'),
        Index('idx_users_day', 'login_id', 'day')
       )
    chart_user_id: Mapped[int] = mapped_column(primary_key=True)
    start_price: Mapped[int] = mapped_column(Integer,CheckConstraint("start_price >= 0"),nullable=False)
    end_price: Mapped[int] = mapped_column(Integer,CheckConstraint("end_price >= 0"),nullable=False)
    max_price: Mapped[int] = mapped_column(Integer,CheckConstraint("max_price >= 0"),nullable=False)
    min_price: Mapped[int] = mapped_column(Integer,CheckConstraint("min_price >= 0"),nullable=False)
    flu_range:  Mapped[int] = mapped_column(Integer)
    flu_range_percent:  Mapped[float] = mapped_column(Float)
    day:  Mapped[int] = mapped_column(Integer,nullable=False)
    login_id: Mapped[str] = mapped_column(String(50),ForeignKey("users.login_id",ondelete="CASCADE"),nullable=False)
    item_code: Mapped[str] = mapped_column(String(10),ForeignKey("items.item_code"),index=True,nullable=False)

    user:Mapped["User"]=relationship(back_populates="chart_users")
    item:Mapped["Item"]=relationship(back_populates="chart_users")
