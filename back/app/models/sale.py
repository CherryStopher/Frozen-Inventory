from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from db.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    date = Column(DateTime)
    enabled = Column(Boolean, default=True)

    client = relationship("Client", back_populates="sales")
    product_sales = relationship("ProductSale", back_populates="sale")
