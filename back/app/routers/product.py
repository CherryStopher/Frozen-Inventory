from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from models import Product
import schemas


router = APIRouter(prefix="/product", tags=["Products"])


@router.get("/")
async def get_products(db: Session = Depends(get_db)):
    data = db.query(Product).all()
    return data


@router.post("/")
async def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name, price=product.price, quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
