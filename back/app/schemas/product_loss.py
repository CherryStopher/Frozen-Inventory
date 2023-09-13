from pydantic import BaseModel


class ProductLoss(BaseModel):
    product_id: int
    quantity: int
    enabled: bool
