from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import Supplier
import schemas
from . import utils


router = APIRouter(prefix="/supplier", tags=["Suppliers"])


@router.get("/get_all")
async def get_suppliers(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(Supplier, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_supplier_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(Supplier, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_supplier(supplier: schemas.Supplier, db: Session = Depends(get_db)):
    try:
        supplier_data = Supplier(
            fantasy_name=supplier.fantasy_name,
            rut=supplier.rut,
            business_name=supplier.business_name,
            contact_name=supplier.contact_name,
            phone=supplier.phone,
            email=supplier.email,
        )
        new_supplier = utils.create_data(db, supplier_data)
        return new_supplier
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the supplier: {str(e)}"
        )


@router.put("/update/{id}")
async def update_supplier(
    id: int, supplier_update: schemas.Supplier, db: Session = Depends(get_db)
):
    try:
        updated_supplier = utils.update_data(
            db, Supplier, id, supplier_update.model_dump(exclude_defaults=True)
        )

        if updated_supplier:
            return updated_supplier
        else:
            raise HTTPException(status_code=404, detail=f"Supplier id {id} not found")

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the supplier: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_supplier(id: int, db: Session = Depends(get_db)):
    try:
        deleted_supplier = utils.delete_data(db, Supplier, id)
        if deleted_supplier:
            return deleted_supplier
        else:
            raise HTTPException(status_code=404, detail=f"Supplier id {id} not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the supplier: {str(e)}"
        )
