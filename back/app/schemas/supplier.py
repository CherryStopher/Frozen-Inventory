from pydantic import BaseModel


class Supplier(BaseModel):
    fantasy_name: str
    rut: str
    business_name: str
    contact_name: str
    phone: str
    email: str
    retirement_address: str
    payment_method: str
