from fastapi import FastAPI
from typing import Union

app = FastAPI()

name = "Default Name"

@app.get("/")
def read_name():
    return {"name": name}

@app.post("/")
def create_name(new_name: str):
    global name
    name = new_name
    return {"name": name}

@app.put("/")
def update_name(new_name: str):
    global name
    name = new_name
    return {"name": name}

@app.delete("/")
def delete_name():
    global name
    name = " "
    return {"name": name}
