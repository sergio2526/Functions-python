from fastapi import FastAPI
from grevillea import Grevillea


app = FastAPI()


@app.get("/")
def read_root(request):
    return {"Hello": "World"}


@app.post("/items/{item}")
def read_item(item : int):
    return {"item_id": item}

handler = Grevillea(app) 