from fastapi import APIRouter, Depends
from ..db.schemas import Product
from ..db.database import get_db
from sqlalchemy.orm import Session
from ..db import models


router = APIRouter(
    prefix="/product",
    tags=["Products"]
)

@router.get("/")
async def get_products(db:Session = Depends(get_db)):
    
    data = db.query(models.Product).all()
    return data

@router.post("/")
async def create_product(product:Product, db:Session = Depends(get_db)):
        
        new_product = models.Product(name=product.name, price=product.price, quantity=product.quantity)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
