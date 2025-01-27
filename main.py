from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    
    return("hello world0000000000000000000000")