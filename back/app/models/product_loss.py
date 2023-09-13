from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.database import Base


class ProductLoss(Base):
    __tablename__ = "product_losses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    enabled = Column(Boolean, default=True)

    product = relationship("Product", back_populates="product_losses")
    movements = relationship("Movement", back_populates="product_loss")
