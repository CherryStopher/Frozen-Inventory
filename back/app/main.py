from fastapi import FastAPI
from .db.database import Base, engine
from .routers import item


def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()
app.include_router(item.router)