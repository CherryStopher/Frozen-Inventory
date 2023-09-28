from pydantic import BaseModel


class ProductSale(BaseModel):
    product_id: int
    sale_id: int
    quantity: int
    unit_price: float
