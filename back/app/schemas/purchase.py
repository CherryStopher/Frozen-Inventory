from pydantic import BaseModel
from datetime import datetime


class Purchase(BaseModel):
    supplier_id: int
    date: datetime
    enabled: bool
