from pydantic import BaseModel


class Client(BaseModel):
    fantasy_name: str
    rut: str
    business_name: str
    nickname: str
    phone: str
    email: str
    address: str
    commune: str
