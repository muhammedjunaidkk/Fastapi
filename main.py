from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    
    return("hello DIVA bbb  aa ccc. ddd eee.............................")

