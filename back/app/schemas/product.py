from pydantic import BaseModel


class Product(BaseModel):
    name: str
    barcode: str
    category: str
    supplier_id: int
    measurement_unit: str
    measurement_unit_quantity: int
