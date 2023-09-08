from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship

from .database import Base 
    
    
class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fantasy_name = Column(String(200))
    rut = Column(String(200))
    business_name = Column(String(200))
    contact_name = Column(String(200))
    phone = Column(String(200))
    email = Column(String(200))
    retirement_address = Column(String(200))
    payment_method = Column(String(200))
    payment_time = Column(String(200))
    product = relationship("Product", back_populates="suppliers")
 
    
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200))
    barcode = Column(String(200))
    category = Column(String(200))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    measurement_unit = Column(String(200))
    measurement_unit_quantity = Column(Integer)
    base = Column(String(200))
    supplier = relationship("Supplier", back_populates="products")