from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200))
    price = Column(Integer)
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())