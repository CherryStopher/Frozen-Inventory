from pydantic import BaseModel


class Movement(BaseModel):
    product_id: int
    product_purchase_id: int
    product_loss_id: int
    product_sale_id: int
    location: str
    quantity: int
    balance: int
    description: str
