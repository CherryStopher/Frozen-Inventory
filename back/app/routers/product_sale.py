from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import ProductSale
import schemas
from . import utils


router = APIRouter(prefix="/product_sale", tags=["Product Sales"])


@router.get("/get_all")
async def get_product_sales(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(ProductSale, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_product_sale_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(ProductSale, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_product_sale(
    product_sale: schemas.ProductSale, db: Session = Depends(get_db)
):
    try:
        product_sale_data = ProductSale(
            product_id=product_sale.product_id,
            sale_id=product_sale.sale_id,
            quantity=product_sale.quantity,
            unit_price=product_sale.unit_price,
        )
        new_product_sale = utils.create_data(db, product_sale_data)
        return new_product_sale
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the product sale: {str(e)}"
        )


@router.put("/update/{id}")
async def update_product_sale(
    id: int, product_sale_update: schemas.ProductSale, db: Session = Depends(get_db)
):
    try:
        updated_product_sale = utils.update_data(
            db, ProductSale, id, product_sale_update.model_dump(exclude_defaults=True)
        )

        if updated_product_sale:
            return updated_product_sale
        else:
            raise HTTPException(
                status_code=404, detail=f"Product sale with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the product sale: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_product_sale(id: int, db: Session = Depends(get_db)):
    try:
        deleted_product_sale = utils.delete_data(db, ProductSale, id)

        if deleted_product_sale:
            return deleted_product_sale
        else:
            raise HTTPException(
                status_code=404, detail=f"Product sale with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the product sale: {str(e)}"
        )
