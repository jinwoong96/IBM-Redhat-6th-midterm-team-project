from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime





class ChartUser(Base):
    __tablename__ = "chart_users"