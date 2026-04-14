from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime




class Wishlist(Base):
    __tablename__ = "wishlists"