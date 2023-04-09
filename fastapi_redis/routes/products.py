from fastapi import APIRouter

from schemas.product import Product

fake_db = [
    {
        "id": "da467f10-b9c5-4f19-bc2a-c0041647b4e7",
        "name": "Jeans",
        "price": 50,
        "date": "2023-03-13 21:26:09.099743"
    },
    {
        "id": "da467f10-b9c5-4f19-bc2a-c77777777777",
        "name": "T-Shirt",
        "price": 25,
        "date": "2023-03-13 21:26:09.099743"
    }
]
products_routes = APIRouter()


@products_routes.get("/example")
def example() -> str:
    return "Example"


@products_routes.get("")
def get_all():
    return fake_db


@products_routes.get("/get/{id}")
def get(id: str):
    try:
        return list(filter(lambda prod: prod["id"] == id, fake_db))[0]
    except Exception as e:
        return e


@products_routes.post("/create", response_model=Product)
def create(product: Product):
    try:
        fake_db.append(product.dict())
        return product
    except Exception as e:
        return e


@products_routes.delete("/delete/{id}")
def delete(id: str):
    try:
        global fake_db
        fake_db = [prod for prod in fake_db if prod["id"] != id]

        return {
            "message": "success"
        }
    except Exception as e:
        return e
