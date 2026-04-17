from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
from .user import User
from .item import Item

class Balance(Base):
    __tablename__ = "balance"
    login_id: Mapped[str] = mapped_column(String(50),ForeignKey("users.login_id", ondelete="CASCADE"),primary_key=True)
    item_code:Mapped[str] = mapped_column(String(10),ForeignKey("items.item_code"),primary_key=True)
    quantity:Mapped[int] = mapped_column(Integer,CheckConstraint("quantity >= 0"),nullable=False) #0
    purchase_price:Mapped[int] = mapped_column(Integer,CheckConstraint("purchase_price >= 0"),nullable=False) #0
    val_price:Mapped[int] = mapped_column(Integer,CheckConstraint("val_price >= 0"),nullable=False) #0
    val_profit_and_loss:Mapped[int] = mapped_column(Integer,nullable=False)
    rate_of_return:Mapped[float] = mapped_column(Float,CheckConstraint("rate_of_return >= -100"),nullable=False) #-100
    
    user:Mapped["User"]=relationship(back_populates="balance")
    item:Mapped["Item"]=relationship(back_populates="balance")