from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
def read_item(item : int):
    item = 12
    return {"item_id": item}
