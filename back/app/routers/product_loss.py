from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import ProductLoss
import schemas
from . import utils


router = APIRouter(prefix="/product_loss", tags=["Product Losses"])


@router.get("/get_all")
async def get_product_losses(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(ProductLoss, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_product_loss_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(ProductLoss, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_product_loss(
    product_loss: schemas.ProductLoss, db: Session = Depends(get_db)
):
    try:
        product_loss_data = ProductLoss(
            product_id=product_loss.product_id,
            quantity=product_loss.quantity,
            enabled=product_loss.enabled,
        )
        new_product_loss = utils.create_data(db, product_loss_data)
        return new_product_loss
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the product loss: {str(e)}"
        )


@router.put("/update/{id}")
async def update_product_loss(
    id: int, product_loss_update: schemas.ProductLoss, db: Session = Depends(get_db)
):
    try:
        updated_product_loss = utils.update_data(
            db, ProductLoss, id, product_loss_update.model_dump(exclude_defaults=True)
        )

        if updated_product_loss:
            return updated_product_loss
        else:
            raise HTTPException(
                status_code=404, detail=f"Product loss with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the product loss: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_product_loss(id: int, db: Session = Depends(get_db)):
    try:
        deleted_product_loss = utils.delete_data(db, ProductLoss, id)

        if deleted_product_loss:
            return deleted_product_loss
        else:
            raise HTTPException(
                status_code=404, detail=f"Product loss with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the product loss: {str(e)}"
        )
