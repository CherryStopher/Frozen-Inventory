from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    id: int
    name: str
    price: int
    quantity: int
    created_at: datetime = datetime.now()