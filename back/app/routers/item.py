from fastapi import APIRouter, Depends
from ..db.schemas import Item
from ..db.database import get_db
from sqlalchemy.orm import Session
from ..db import models


router = APIRouter(
    prefix="/item",
    tags=["Items"]
)

@router.get("/")
async def get_items(db:Session = Depends(get_db)):
    
    data = db.query(models.Item).all()
    return data

@router.post("/")
async def create_item(item:Item, db:Session = Depends(get_db)):
        
        new_item = models.Item(name=item.name, price=item.price, quantity=item.quantity)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
