from pydantic import BaseModel


class ProductPurchase(BaseModel):
    purchase_id: int
    product_id: int
    quantity: int
    unit_price: int
