from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime




class ChartInit(Base):
    __tablename__ = "chart_inits"