from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import Purchase
import schemas
from . import utils


router = APIRouter(prefix="/purchase", tags=["Purchase"])


@router.get("/get_all")
async def get_purchases(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(Purchase, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_purchase_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(Purchase, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_purchase(purchase: schemas.Purchase, db: Session = Depends(get_db)):
    try:
        purchase_data = Purchase(
            supplier_id=purchase.supplier_id,
            date=purchase.date,
            enabled=purchase.enabled,
        )
        new_purchase = utils.create_data(db, purchase_data)
        return new_purchase
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the purchase: {str(e)}"
        )


@router.put("/update/{id}")
async def update_purchase(
    id: int, purchase_update: schemas.Purchase, db: Session = Depends(get_db)
):
    try:
        updated_purchase = utils.update_data(
            db, Purchase, id, purchase_update.model_dump(exclude_defaults=True)
        )

        if updated_purchase:
            return updated_purchase
        else:
            raise HTTPException(
                status_code=404, detail=f"Purchase with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the purchase: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_purchase(id: int, db: Session = Depends(get_db)):
    try:
        deleted_purchase = utils.delete_data(db, Purchase, id)
        if deleted_purchase:
            return deleted_purchase
        else:
            raise HTTPException(
                status_code=404, detail=f"Purchase with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the purchase: {str(e)}"
        )
