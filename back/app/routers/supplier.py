from fastapi import APIRouter, Depends
from ..db.schemas import Supplier
from ..db.database import get_db
from sqlalchemy.orm import Session
from ..db import models


router = APIRouter(
    prefix="/supplier",
    tags=["Suppliers"]
)

@router.get("/")
async def get_suppliers(db:Session = Depends(get_db)):
    
    data = db.query(models.Supplier).all()
    return data

@router.post("/")
async def create_supplier(supplier:Supplier, db:Session = Depends(get_db)):
        
        new_supplier = models.Supplier(name=supplier.name, price=supplier.price, quantity=supplier.quantity)
        db.add(new_supplier)
        db.commit()
        db.refresh(new_supplier)
        return new_supplier