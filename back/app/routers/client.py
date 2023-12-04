from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from models import Client
import schemas
from . import utils


router = APIRouter(prefix="/clients", tags=["Clients"])


@router.get("/get_all")
async def get_clients(db: Session = Depends(get_db)):
    try:
        data = db.query(Client).all()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{id}")
async def get_client_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = db.query(Client).filter(Client.id == id).first()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create")
async def create_client(client: schemas.Client, db: Session = Depends(get_db)):
    try:
        client_data = Client(
            fantasy_name=client.fantasy_name,
            rut=client.rut,
            business_name=client.business_name,
            contact_name=client.contact_name,
            phone=client.phone,
            email=client.email,
        )
        new_client = utils.create_data(db, client_data)
        return new_client
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to create the client: {str(e)}"
        )


@router.put("/update/{id}")
async def update_client(
    id: int, client_update: schemas.Client, db: Session = Depends(get_db)
):
    try:
        updated_client = utils.update_data(
            db, Client, id, client_update.model_dump(exclude_defaults=True)
        )

        if updated_client:
            return updated_client
        else:
            raise HTTPException(status_code=404, detail=f"Client id {id} not found")

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to update the client: {str(e)}"
        )


@router.delete("/delete/{id}")
async def delete_client(id: int, db: Session = Depends(get_db)):
    try:
        deleted_client = utils.delete_data(db, Client, id)
        if deleted_client:
            return deleted_client
        else:
            raise HTTPException(status_code=404, detail=f"Client id {id} not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error to delete the client: {str(e)}"
        )
