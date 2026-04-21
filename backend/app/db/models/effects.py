from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String,Float, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer, UniqueConstraint
from typing import Optional, List, TYPE_CHECKING


if TYPE_CHECKING:
    from .news import News
class Effects(Base):
    __tablename__ = "effects"

    __table_args__ = (
        CheckConstraint("flu_min <= flu_max", name="chk_effects_flu_range"),
        UniqueConstraint("news_id", "category_name", name="uq_effects_news_id_category_name")
    )

    effect_id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    flu_min: Mapped[float] = mapped_column(Float, CheckConstraint("flu_min >= -30", name="chk_effects_flu_min"), nullable=False)
    flu_max: Mapped[float] = mapped_column(Float, CheckConstraint("flu_max <= 30", name="chk_effects_flu_max"), nullable=False)
    news_id: Mapped[int] = mapped_column(Integer,ForeignKey("news.news_id"),nullable=False)
    category_name: Mapped[str] = mapped_column(String(20),nullable=False,index=True)
   
    news: Mapped["News"] = relationship(back_populates="effects")