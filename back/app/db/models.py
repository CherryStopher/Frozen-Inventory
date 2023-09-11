from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship

from .database import Base 
    
    
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
    
    purchase = relationship("Purchase", back_populates="suppliers")
    product = relationship("Product", back_populates="suppliers")
    
    
class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fantasy_name = Column(String(200))
    rut = Column(String(200))
    business_name = Column(String(200))
    nickname = Column(String(200))
    contact_name = Column(String(200))
    phone = Column(String(200))
    email = Column(String(200))
    adress = Column(String(200))
    commune = Column(String(200))
    payment_method = Column(String(200))
    
    sale = relationship("Sale", back_populates="clients")
 
 
class Purchase(Base):
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    date = Column(DateTime)
    enabled = Column(Boolean, default=True)
    
    supplier = relationship("Supplier", back_populates="purchases")
    product_purchase = relationship("ProductPurchase", back_populates="purchases")
    
    
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
    movement = relationship("Movement", back_populates="products")


class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    date = Column(DateTime)
    enabled = Column(Boolean, default=True)
    
    client = relationship("Client", back_populates="sales")
    product_sale = relationship("ProductSale", back_populates="sales")
    
    
class ProductPurchase(Base):
    __tablename__ = "product_purchases"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    unit_price = Column(Integer)
    
    purchase = relationship("Purchase", back_populates="product_purchases")
    product = relationship("Product", back_populates="product_purchases")
    movement = relationship("Movement", back_populates="product_purchases")
    

class ProductLoss(Base):
    __tablename__ = "product_losses"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    enabled = Column(Boolean, default=True)
    
    product = relationship("Product", back_populates="product_losses")
    movement = relationship("Movement", back_populates="product_losses")
    

class ProductSale(Base):
    __tablename__ = "product_sales"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    sale_id = Column(Integer, ForeignKey("sales.id"))
    quantity = Column(Integer)
    unit_price = Column(Integer)
    
    product = relationship("Product", back_populates="product_sales")
    sale = relationship("Product", back_populates="product_sales")
    movement = relationship("Movement", back_populates="product_sales")
    

class Movement(Base):
    __tablename__ = "movements"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product_purchase_id = Column(Integer, ForeignKey("product_purchases.id"), nullable=True)
    product_loss_id = Column(Integer, ForeignKey("product_losses.id"), nullable=True)
    product_sale_id = Column(Integer, ForeignKey("product_sales.id"), nullable=True)
    location = Column(String(200),nullable=False)
    quantity = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)
    
    product_purchase = relationship("ProductPurchase", back_populates="movements")
    product_loss = relationship("ProductLoss", back_populates="movements")
    product_sale = relationship("ProductSale", back_populates="movements")