from pydantic import BaseModel
from datetime import datetime


class Sale(BaseModel):
    client_id: int
    date: datetime
    enabled: bool
