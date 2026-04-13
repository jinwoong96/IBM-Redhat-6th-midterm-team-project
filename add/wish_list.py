from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, Integer, ForeignKey
from typing import Optional, List, TYPE_CHECKING

class Wish_list(Base):
    __tablename__ = "wishlists"
    wishlist_id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"),String(50),nullable=False)
    item_code: Mapped[str] = mapped_column(ForeignKey("items.item_code", ondelete="CASCADE"),String(10),nullable=False)
