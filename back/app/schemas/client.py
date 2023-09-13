from pydantic import BaseModel


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
