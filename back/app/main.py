from fastapi import FastAPI
from routers import product, supplier, sale, purchase, movement


app = FastAPI()
app.include_router(product.router)
app.include_router(supplier.router)
app.include_router(sale.router)
app.include_router(purchase.router)
app.include_router(movement.router)
