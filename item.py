from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, Integer, ForeignKey,Float
from typing import Optional, List, TYPE_CHECKING



class Item(Base):
    __tablename__ = "items"
    item_code: Mapped[str] = mapped_column(String(10),primary_key=True,nullable=False)
    item_name: Mapped[str] = mapped_column(String(50),nullable=False)
    item_category: Mapped[str] = mapped_column(String(50),nullable=False)
    curr_price: Mapped[int] = mapped_column(Integer, nullable=False)
    flu_range: Mapped[int] = mapped_column(Integer)
    flu_range_percent: Mapped[float] = mapped_column(Float)
