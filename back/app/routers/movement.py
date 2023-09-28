from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import Movement
import schemas
from . import utils


router = APIRouter(prefix="/movement", tags=["Movements"])


@router.get("/get_all")
async def get_movements(db: Session = Depends(get_db)):
    try:
        data = utils.get_all_data(Movement, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_movement_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = utils.get_data_by_id(Movement, db, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_movement(movement: schemas.Movement, db: Session = Depends(get_db)):
    try:
        movement_data = Movement(
            product_id=movement.product_id,
            product_purchase_id=movement.product_purchase_id,
            product_loss_id=movement.product_loss_id,
            product_sale_id=movement.product_sale_id,
            location=movement.location,
            quantity=movement.quantity,
            balance=movement.balance,
            description=movement.description,
        )
        new_movement = utils.create_data(db, movement_data)
        return new_movement
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the movement: {str(e)}"
        )


@router.put("/update/{id}")
async def update_movement(
    id: int, movement_update: schemas.Movement, db: Session = Depends(get_db)
):
    try:
        updated_movement = utils.update_data(
            db, Movement, id, movement_update.model_dump(exclude_defaults=True)
        )

        if updated_movement:
            return updated_movement
        else:
            raise HTTPException(
                status_code=404, detail=f"Movement with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the movement: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_movement(id: int, db: Session = Depends(get_db)):
    try:
        deleted_movement = utils.delete_data(db, Movement, id)

        if deleted_movement:
            return deleted_movement
        else:
            raise HTTPException(
                status_code=404, detail=f"Movement with id {id} not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the movement: {str(e)}"
        )
