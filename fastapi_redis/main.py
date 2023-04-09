from fastapi import FastAPI
from routes.products import products_routes

app = FastAPI()

app.include_router(products_routes, prefix="/products")
