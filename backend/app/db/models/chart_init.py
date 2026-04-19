<<<<<<< HEAD
from database import Base
=======
from app.db.database import Base
>>>>>>> origin/main
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer,UniqueConstraint
from typing import Optional, List, TYPE_CHECKING
from .item import Item
class ChartInit(Base):
<<<<<<< HEAD
    __tablename__ = "chart_init"
=======
    __tablename__ = "chart_inits"
>>>>>>> origin/main

    __table_args__ = (
        UniqueConstraint('item_code', 'day', name='uix_chart_init_item_code_day'),
    )
    chart_id: Mapped[int] = mapped_column(Integer,primary_key=True)    
    item_code: Mapped[str] = mapped_column(String(10),ForeignKey("items.item_code"),index=True,nullable=False)
    start_price: Mapped[int] = mapped_column(Integer,CheckConstraint("start_price >= 0"),nullable=False)
    end_price: Mapped[int] = mapped_column(Integer,CheckConstraint("end_price >= 0"),nullable=False)
    max_price: Mapped[int] = mapped_column(Integer,CheckConstraint("max_price >= 0"),nullable=False)
    min_price: Mapped[int] = mapped_column(Integer,CheckConstraint("min_price >= 0"),nullable=False)
    flu_range:  Mapped[int] = mapped_column(Integer)
    flu_range_percent:  Mapped[float] = mapped_column(Float)
    day: Mapped[int] = mapped_column(Integer,nullable=False)
    
<<<<<<< HEAD
    item: Mapped["Item"]=relationship(back_populates="balance")
=======
    item: Mapped["Item"]=relationship(back_populates="chart_inits")
>>>>>>> origin/main
