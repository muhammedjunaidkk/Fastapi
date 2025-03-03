from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    Statement="item_id :" ,item_id, "message : item number", item_id ,"is flagged"
    return Statement
