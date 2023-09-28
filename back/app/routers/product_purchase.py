from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import ProductPurchase
import schemas
from . import utils


router = APIRouter(prefix="/product_purchase", tags=["Product Purchases"])


@router.get("/get_all")
async def get_product_purchases(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(ProductPurchase, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_product_purchase_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(ProductPurchase, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_product_purchase(
    product_purchase: schemas.ProductPurchase, db: Session = Depends(get_db)
):
    try:
        product_purchase_data = ProductPurchase(
            purchase_id=product_purchase.purchase_id,
            product_id=product_purchase.product_id,
            quantity=product_purchase.quantity,
            unit_price=product_purchase.unit_price,
        )
        new_product_purchase = utils.create_data(db, product_purchase_data)
        return new_product_purchase
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the product purchase: {str(e)}"
        )


@router.put("/update/{id}")
async def update_product_purchase(
    id: int,
    product_purchase_update: schemas.ProductPurchase,
    db: Session = Depends(get_db),
):
    try:
        updated_product_purchase = utils.update_data(
            db,
            ProductPurchase,
            id,
            product_purchase_update.model_dump(exclude_defaults=True),
        )

        if updated_product_purchase:
            return updated_product_purchase
        else:
            raise HTTPException(
                status_code=404, detail=f"Product purchase with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the product purchase: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_product_purchase(id: int, db: Session = Depends(get_db)):
    try:
        deleted_product_purchase = utils.delete_data(db, ProductPurchase, id)

        if deleted_product_purchase:
            return deleted_product_purchase
        else:
            raise HTTPException(
                status_code=404, detail=f"Product purchase with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the product purchase: {str(e)}"
        )
