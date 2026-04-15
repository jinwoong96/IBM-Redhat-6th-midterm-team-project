from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
from chart_user import ChartUser
from trade import Trade
from wish_list import Wishlist
from balance import Balance
from chart_init import ChartInit
if TYPE_CHECKING:
    from .chart_user import ChartUser
    from .trade import Trade
    from .wish_list import Wishlist
    from .balance import Balance
    from .chart_init import ChartInit

class Item(Base):
    __tablename__ = "items"
    item_code: Mapped[str] = mapped_column(String(10),primary_key=True,nullable=False)
    item_name: Mapped[str] = mapped_column(String(50),nullable=False)
    category_name: Mapped[str] = mapped_column(String(20),index=True,nullable=False)
   
    chartuser:Mapped[list["ChartUser"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    trade:Mapped[list["Trade"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    wishlist:Mapped[list["Wishlist"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    balance:Mapped[list["Balance"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    chartinit:Mapped[list["ChartInit"]] = relationship(back_populates="item", cascade="all, delete-orphan")