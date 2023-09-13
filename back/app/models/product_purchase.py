from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class ProductPurchase(Base):
    __tablename__ = "product_purchases"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    unit_price = Column(Integer)

    purchase = relationship("Purchase", back_populates="product_purchases")
    product = relationship("Product", back_populates="product_purchases")
    movements = relationship("Movement", back_populates="product_purchase")
