from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING

class Item(Base):
    __tablename__ = "items"
    item_code: Mapped[str] = mapped_column(String(10),primary_key=True,nullable=False)
    item_name: Mapped[str] = mapped_column(String(50),nullable=False)
    category_id: Mapped[int] = mapped_column(Integer,ForeignKey("category.category_id"),nullable=False)
    curr_price: Mapped[int] = mapped_column(Integer,CheckConstraint("curr_price>= 0"),nullable=False)
    flu_range: Mapped[int] = mapped_column(Integer)
    flu_range_percent: Mapped[float] = mapped_column(Float)
    