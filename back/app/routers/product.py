from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import Product
import schemas
from . import utils


router = APIRouter(prefix="/product", tags=["Products"])


@router.get("/")
async def get_products(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(Product, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}")
async def get_product_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(Product, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
async def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    try:
        product_data = Product(
            name=product.name,
            barcode=product.barcode,
            category=product.category,
            supplier_id=product.supplier_id,
            measurement_unit=product.measurement_unit,
            measurement_unit_quantity=product.measurement_unit_quantity,
        )
        new_product = utils.create_data(db, product_data)
        return new_product
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the product: {str(e)}"
        )


@router.put("/{id}")
async def update_product(
    id: int, product_update: schemas.Product, db: Session = Depends(get_db)
):
    try:
        updated_product = utils.update_data(
            db, Product, id, product_update.model_dump(exclude_defaults=True)
        )

        if updated_product:
            return updated_product
        else:
            raise HTTPException(
                status_code=404, detail=f"Product with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the product: {str(e)}"
        )


@router.delete("/{id}")
async def delete_product(id: int, db: Session = Depends(get_db)):
    try:
        deleted_product = utils.delete_data(db, Product, id)
        if deleted_product:
            return deleted_product
        else:
            raise HTTPException(status_code=404, detail=f"Product id {id} not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the product: {str(e)}"
        )
