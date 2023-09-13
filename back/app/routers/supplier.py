from fastapi import APIRouter, Depends
import schemas
from db.database import get_db
from sqlalchemy.orm import Session
from models import Supplier


router = APIRouter(prefix="/supplier", tags=["Suppliers"])


@router.get("/")
async def get_suppliers(db: Session = Depends(get_db)):
    data = db.query(Supplier).all()
    return data


@router.post("/")
async def create_supplier(supplier: schemas.Supplier, db: Session = Depends(get_db)):
    new_supplier = Supplier(
        name=supplier.name, price=supplier.price, quantity=supplier.quantity
    )
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier
