from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class ProductSale(Base):
    __tablename__ = "product_sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    sale_id = Column(Integer, ForeignKey("sales.id"))
    quantity = Column(Integer)
    unit_price = Column(Integer)

    product = relationship("Product", back_populates="product_sales")
    sale = relationship("Sale", back_populates="product_sales")
    movements = relationship("Movement", back_populates="product_sale")
