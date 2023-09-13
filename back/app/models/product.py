from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.database import Base


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
    movements = relationship("Movement", back_populates="product")
    product_losses = relationship("ProductLoss", back_populates="product")
    product_purchases = relationship("ProductPurchase", back_populates="product")
    product_sales = relationship("ProductSale", back_populates="product")
