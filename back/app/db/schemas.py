from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    name: str
    barcode: str
    category: str
    supplier_id: int
    measurement_unit: str
    measurement_unit_quantity: int
    base: str
    
    
class Supplier(BaseModel):
    fantasy_name: str
    rut: str
    business_name: str
    contact_name: str
    phone: str
    email: str
    retirement_address: str
    payment_method: str
    payment_time: str