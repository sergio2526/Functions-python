from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/{item}")
def read_item(item : int):
    return {"item_id": item}
