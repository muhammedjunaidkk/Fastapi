from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    
    return("DIVA         DIVA         DIVA           DIVA")

