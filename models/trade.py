from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
import time
class Trade(Base):
    __tablename__ = "trades"
    trade_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id",ondelete="CASCADE"),index=True)
    item_code: Mapped[str] = mapped_column(Integer(10),ForeignKey("items.item_code"),index=True)
    buy_type: Mapped[str] = mapped_column(Integer(10),nullable=False)
    price: Mapped[int] = mapped_column(Integer,CheckConstraint("price >= 0"),nullable=False)
    quantity: Mapped[int] = mapped_column(Integer,CheckConstraint("quantity >= 0"),nullable=False)
    trade_day: Mapped[int] = mapped_column(
        Integer,
        CheckConstraint("trade_day >= 0"), 
        default=lambda: int(time.time()), 
        nullable=False
    )