from sqlalchemy.orm import Session
from models import *
from db.database import Base
import schemas
from pydantic import BaseModel


def get_all_data(model: Base, db: Session):
    data = db.query(model).all()
    return data


def get_data_by_id(model: Base, db: Session, id: int):
    data = db.query(model).filter(model.id == id).first()
    return data


def create_data(db: Session, dataModel: BaseModel):
    db.add(dataModel)
    db.commit()
    db.refresh(dataModel)
    return dataModel


def update_data(db: Session, dataModel, id: int, update_data):
    existing_data = db.query(dataModel).filter(dataModel.id == id).first()
    if existing_data:
        for key, value in update_data.items():
            setattr(existing_data, key, value)
        db.commit()
        db.refresh(existing_data)
        return update_data
    else:
        return None


def delete_data(db: Session, dataModel, id: int):
    existing_data = db.query(dataModel).filter(dataModel.id == id).first()
    if existing_data:
        db.delete(existing_data)
        db.commit()
        return existing_data
    else:
        return None
