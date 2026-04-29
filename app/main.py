from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="Mi API FastAPI",
    description="API de ejemplo construida con FastAPI y Python",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Hola mundo. Te saludo desde FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
