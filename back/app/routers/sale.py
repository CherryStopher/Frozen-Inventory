from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import Sale
import schemas
from . import utils


router = APIRouter(prefix="/sale", tags=["Sales"])


@router.get("/")
async def get_sales(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(Sale, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}")
async def get_sale_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(Sale, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
async def create_sale(sale: schemas.Sale, db: Session = Depends(get_db)):
    try:
        sale_data = Sale(
            client_id=sale.client_id,
            date=sale.date,
            enabled=sale.enabled,
        )
        new_sale = utils.create_data(db, sale_data)
        return new_sale
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the sale: {str(e)}"
        )


@router.put("/{id}")
async def update_sale(
    id: int, sale_update: schemas.Sale, db: Session = Depends(get_db)
):
    try:
        updated_sale = utils.update_data(
            db, Sale, id, sale_update.model_dump(exclude_defaults=True)
        )

        if updated_sale:
            return updated_sale
        else:
            raise HTTPException(status_code=404, detail=f"Sale with id {id} not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the sale: {str(e)}"
        )


@router.delete("/{id}")
async def delete_sale(id: int, db: Session = Depends(get_db)):
    try:
        deleted_sale = utils.delete_data(db, Sale, id)
        if deleted_sale:
            return deleted_sale
        else:
            raise HTTPException(status_code=404, detail=f"Sale with id {id} not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the sale: {str(e)}"
        )
