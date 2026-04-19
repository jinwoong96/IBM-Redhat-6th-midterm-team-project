<<<<<<< HEAD
from database import Base
=======
from app.db.database import Base
>>>>>>> origin/main
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .chart_user import ChartUser
    from .trade import Trade
<<<<<<< HEAD
    from .wishlist import WishList
=======
    from .wishlist import Wishlist
>>>>>>> origin/main
    from .balance import Balance
    from .chart_init import ChartInit

class Item(Base):
    __tablename__ = "items"
    item_code: Mapped[str] = mapped_column(String(10),primary_key=True,nullable=False)
    item_name: Mapped[str] = mapped_column(String(50),nullable=False)
    category_name: Mapped[str] = mapped_column(String(20),index=True,nullable=False)
   
<<<<<<< HEAD
    chartuser:Mapped[list["ChartUser"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    trade:Mapped[list["Trade"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    wishlist:Mapped[list["WishList"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    balance:Mapped[list["Balance"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    chartinit:Mapped[list["ChartInit"]] = relationship(back_populates="item", cascade="all, delete-orphan")
=======
    chart_users:Mapped[list["ChartUser"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    trades:Mapped[list["Trade"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    wishlists:Mapped[list["Wishlist"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    balances:Mapped[list["Balance"]] = relationship(back_populates="item", cascade="all, delete-orphan")
    chart_inits:Mapped[list["ChartInit"]] = relationship(back_populates="item", cascade="all, delete-orphan")
>>>>>>> origin/main
