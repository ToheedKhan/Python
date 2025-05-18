import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_stock: bool = None


# Home route
@app.get("/")
def read_root():

    return {"message": "Welcome to FASTAPI backend!"}

# Read an item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int,):
    return {"item_id": item_id}

# Create a new item
@app.post("/items/")
def create_item(item: Item):
    return {"item_created": item}

