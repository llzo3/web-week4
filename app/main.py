from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "Hello": "World!"}

@app.get("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}