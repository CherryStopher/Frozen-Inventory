from fastapi import FastAPI
from routers import product, supplier


app = FastAPI()
app.include_router(product.router)
app.include_router(supplier.router)
