from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.database import Base


class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product_purchase_id = Column(
        Integer, ForeignKey("product_purchases.id"), nullable=True
    )
    product_loss_id = Column(Integer, ForeignKey("product_losses.id"), nullable=True)
    product_sale_id = Column(Integer, ForeignKey("product_sales.id"), nullable=True)
    location = Column(String(200), nullable=False)
    quantity = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)

    product = relationship("Product", back_populates="movements")
    product_purchase = relationship("ProductPurchase", back_populates="movements")
    product_loss = relationship("ProductLoss", back_populates="movements")
    product_sale = relationship("ProductSale", back_populates="movements")
