from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
db = {}

class Address(BaseModel):
    address: str
    coordinates: str

@app.post("/")
def create(addr: Address):
    db[addr.address] = addr.coordinates
    return {"address": addr}

@app.get("/")
def get_all():
    return db

@app.delete("/")
def delete_address(address: str):
    del db[address]
    return db

@app.put("/")
def update_address(addr: Address):
    db[addr.address] = addr.coordinates
    return db

