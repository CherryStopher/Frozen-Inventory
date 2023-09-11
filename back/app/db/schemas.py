from pydantic import BaseModel
from datetime import datetime

class Supplier(BaseModel):
    fantasy_name: str
    rut: str
    business_name: str
    contact_name: str
    phone: str
    email: str
    retirement_address: str
    payment_method: str
    

class Client(BaseModel):
    fantasy_name: str
    rut: str
    business_name: str
    nickname: str
    contact_name: str
    phone: str
    email: str
    adress: str
    commune: str
    payment_method: str
    

class Purchase(BaseModel):
    supplier_id: int
    date: datetime
    enabled: bool
    

class Product(BaseModel):
    name: str
    barcode: str
    category: str
    supplier_id: int
    measurement_unit: str
    measurement_unit_quantity: int
    base: str
    

class Sale(BaseModel):
    client_id: int
    date: datetime
    enabled: bool
    

class ProductPurchase(BaseModel):
    purchase_id: int
    product_id: int
    quantity: int
    unit_price: int


class ProductLoss(BaseModel):
    product_id: int
    quantity: int
    enabled: bool
    
    
class ProductSale(BaseModel):
    product_id: int
    sale_id: int
    quantity: int
    unit_price: int
    

class Movement(BaseModel):
    product_id: int
    product_purchase_id: int
    product_loss_id: int
    product_sale_id: int
    location: str
    quantity: int
    balance: int
    description: str