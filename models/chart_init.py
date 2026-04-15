from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
from item import Item
class ChartInit(Base):
    __tablename__ = "chart_init"
    chart_id: Mapped[int] = mapped_column(Integer,primary_key=True)    
    item_code: Mapped[str] = mapped_column(ForeignKey("items.item_code"),String(10),index=True,nullable=False)
    start_price: Mapped[int] = mapped_column(Integer,CheckConstraint("start_price >= 0"),nullable=False)
    end_price: Mapped[int] = mapped_column(Integer,CheckConstraint("end_price >= 0"),nullable=False)
    max_price: Mapped[int] = mapped_column(Integer,CheckConstraint("max_price >= 0"),nullable=False)
    min_price: Mapped[int] = mapped_column(Integer,CheckConstraint("min_price >= 0"),nullable=False)
    flu_range:  Mapped[int] = mapped_column(Integer)
    flu_range_percent:  Mapped[float] = mapped_column(Float)
    day: Mapped[int] = mapped_column(Integer,nullable=False)
    
    item: Mapped["Item"]=relationship(back_populates="balance")