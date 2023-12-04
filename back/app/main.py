from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    product,
    supplier,
    client,
    sale,
    purchase,
    product_purchase,
    product_loss,
    product_sale,
    movement,
)

app = FastAPI()
app.include_router(product.router)
app.include_router(supplier.router)
app.include_router(client.router)
app.include_router(sale.router)
app.include_router(purchase.router)
app.include_router(product_purchase.router)
app.include_router(product_loss.router)
app.include_router(product_sale.router)
app.include_router(movement.router)


origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
