from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
from ranking import Ranking
from chart_user import ChartUser
from trade import Trade
from news_user import NewsUser
from wish_list import Wishlist
from balance import Balance
if TYPE_CHECKING:
    from .ranking import Ranking
    from .chart_user import ChartUser
    from .trade import Trade
    from .news_user import NewsUser
    from .wish_list import Wishlist
    from .balance import Balance

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[str] = mapped_column(String(50),primary_key=True)
    user_nickname: Mapped[str] = mapped_column(String(50),nullable=False, unique=True)
    user_password: Mapped[str] = mapped_column(String(50),nullable=False)
    money: Mapped[int] = mapped_column(Integer,CheckConstraint("money >= 0"),default=50000000)
    valuation: Mapped[int] = mapped_column(Integer,CheckConstraint("valuation >= 0"),default=0)
    created_at: Mapped[datetime]= mapped_column(TIMESTAMP, server_default=func.now())
    refresh_token: Mapped[Optional[str]]=mapped_column(String(255), nullable=True)

   
    ranking:Mapped[list["Ranking"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    chartuser:Mapped[list["ChartUser"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    trade:Mapped[list["Trade"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    newsuser:Mapped[list["NewsUser"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    wishlist:Mapped[list["Wishlist"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    balance:Mapped[list["Balance"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    #posts:Mapped[list["Post"]] = relationship(back_populates="owner", cascade="all, delete-orphan")