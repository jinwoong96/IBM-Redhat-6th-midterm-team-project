from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer
from typing import Optional, List, TYPE_CHECKING
from user import User
from item import Item
class Wishlist(Base):
    __tablename__ = "wish_lists"
    wishlist_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.user_id",ondelete="CASCADE"),String(50), nullable=False)
    item_code: Mapped[str] = mapped_column(ForeignKey("items.item_code",ondelete="CASCADE"),String(10),nullable=False)
    
    user:Mapped["User"]=relationship(back_populates="wishlist")
    item:Mapped["Item"]=relationship(back_populates="wishlist")