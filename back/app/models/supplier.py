from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fantasy_name = Column(String(200), nullable=False)
    rut = Column(String(200), nullable=False)
    business_name = Column(String(200), nullable=False)
    contact_name = Column(String(200), nullable=False)
    phone = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    retirement_address = Column(String(200), nullable=False)
    payment_method = Column(String(200), nullable=False)

    purchases = relationship("Purchase", back_populates="supplier")
    products = relationship("Product", back_populates="supplier")
