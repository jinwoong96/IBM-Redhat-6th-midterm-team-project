from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

class Balance(Base):
    __tablename__ = "balance"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"),primary_key=True)
    item_code:Mapped[str] = mapped_column(String(10),ForeignKey("items.item_code"),primary_key=True)
    quantity:Mapped[int] = mapped_column(Integer,nullable=False)
    purchase_price:Mapped[int] = mapped_column(Integer,nullable=False)
    val_price:Mapped[int] = mapped_column(Integer,nullable=False)
    val_profit_and_loss:Mapped[int] = mapped_column(Integer,nullable=False)
    rate_of_return:Mapped[float] = mapped_column(Float,nullable=False)