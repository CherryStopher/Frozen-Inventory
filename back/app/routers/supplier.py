from fastapi import APIRouter, Depends
import schemas
from db.database import get_db
from sqlalchemy.orm import Session
from models import Supplier
from fastapi import HTTPException


router = APIRouter(prefix="/supplier", tags=["Suppliers"])


@router.get("/")
async def get_suppliers(db: Session = Depends(get_db)): 
    try:
        data = db.query(Supplier).all()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
async def create_supplier(supplier: schemas.Supplier, db: Session = Depends(get_db)):
    new_supplier = Supplier(
        name=supplier.name, price=supplier.price, quantity=supplier.quantity
    )
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier
