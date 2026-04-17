from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .ranking import Ranking
    from .chart_user import ChartUser
    from .trade import Trade
    from .news_user import NewsUser
    from .wishlist import WishList
    from .balance import Balance

class User(Base):
    __tablename__ = "users"
    login_id: Mapped[str] = mapped_column(String(50),primary_key=True)
    user_nickname: Mapped[str] = mapped_column(String(50),nullable=False, unique=True)
    user_password: Mapped[str] = mapped_column(String(255),nullable=False)
    money: Mapped[int] = mapped_column(Integer,CheckConstraint("money >= 0"),server_default="50000000")
    valuation: Mapped[int] = mapped_column(Integer,CheckConstraint("valuation >= 0"),server_default="0")
    created_at: Mapped[datetime]= mapped_column(TIMESTAMP, server_default=func.now())
    refresh_token: Mapped[Optional[str]]=mapped_column(String(255), nullable=True)

    # Optional을 쓰는 이유: 유저가 생성된 직후에는 랭킹 데이터가 없을 수 있기 때문입니다.
    ranking: Mapped[Optional["Ranking"]] = relationship(
        back_populates="user", 
        cascade="all, delete-orphan", 
        uselist=False 
    )
    chartuser:Mapped[list["ChartUser"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    trade:Mapped[list["Trade"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    newsuser:Mapped[list["NewsUser"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    wishlist:Mapped[list["WishList"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    balance:Mapped[list["Balance"]] = relationship(back_populates="user",cascade="all, delete-orphan")
    