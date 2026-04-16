from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime



class Balance(Base):
    __tablename__ = "balances"
    pass