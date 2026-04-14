from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime



class Newsuser(Base):
    __tablename__ = "news_user"