<<<<<<< HEAD
from database import Base
=======
from app.db.database import Base
>>>>>>> origin/main
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey, CheckConstraint, Integer,UniqueConstraint
from typing import Optional, List, TYPE_CHECKING
from .user import User
from .item import Item
<<<<<<< HEAD
class WishList(Base):
    __tablename__ = "wishlist"
=======
class Wishlist(Base):
    __tablename__ = "wishlists"
>>>>>>> origin/main
    
    __table_args__ = (
        UniqueConstraint('login_id', 'item_code', name='uix_login_item'),
    )

    wishlist_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    login_id: Mapped[str] = mapped_column(String(50),ForeignKey("users.login_id",ondelete="CASCADE"), nullable=False)
    item_code: Mapped[str] = mapped_column(String(10),ForeignKey("items.item_code",ondelete="CASCADE"),nullable=False)
    
<<<<<<< HEAD
    user:Mapped["User"]=relationship(back_populates="wishlist")
    item:Mapped["Item"]=relationship(back_populates="wishlist")
=======
    user:Mapped["User"]=relationship(back_populates="wishlists")
    item:Mapped["Item"]=relationship(back_populates="wishlists")
>>>>>>> origin/main
