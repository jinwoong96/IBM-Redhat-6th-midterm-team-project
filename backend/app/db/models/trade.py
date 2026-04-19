<<<<<<< HEAD
from database import Base
=======
from app.db.database import Base
>>>>>>> origin/main
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
import time
from .user import User
from .item import Item
class Trade(Base):
    __tablename__ = "trades"
    trade_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    buy_type: Mapped[str] = mapped_column(
        String(10), 
        CheckConstraint("buy_type IN ('buy', 'sell')", name="chk_trade_buy_type"), 
        nullable=False
    )
    price: Mapped[int] = mapped_column(Integer,CheckConstraint("price >= 0"),nullable=False)
    quantity: Mapped[int] = mapped_column(Integer,CheckConstraint("quantity >= 0"),nullable=False)
    trade_day: Mapped[int] = mapped_column(
        Integer,
        CheckConstraint("trade_day >= 0"), 
        default=lambda: int(time.time()), 
        nullable=False
    )
    login_id: Mapped[str] = mapped_column(String(50),ForeignKey("users.login_id",ondelete="CASCADE"),index=True)
    item_code: Mapped[str] = mapped_column(String(10),ForeignKey("items.item_code"),index=True)  
   
<<<<<<< HEAD
    user:Mapped["User"]=relationship(back_populates="trade")
    item:Mapped["Item"]=relationship(back_populates="trade")
=======
    user:Mapped["User"]=relationship(back_populates="trades")
    item:Mapped["Item"]=relationship(back_populates="trades")
>>>>>>> origin/main
