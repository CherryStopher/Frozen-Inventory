from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from db.database import Base


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    date = Column(DateTime)
    enabled = Column(Boolean, default=True)

    supplier = relationship("Supplier", back_populates="purchases")
    product_purchases = relationship("ProductPurchase", back_populates="purchase")
