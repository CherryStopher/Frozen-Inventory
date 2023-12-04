from pydantic import BaseModel


class Client(BaseModel):
    name: str
    rut: str
    nickname: str
    phone: str
    email: str
    address: str
    commune: str
