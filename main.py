# main.py
from fastapi import FastAPI, HTTPException
from database import execute_insert
import os

app = FastAPI()

@app.get("/")
def add_name(name: str = "Default Name"):
    """Inserts a name into the appropriate table."""
    table_name = "uatinfo" if os.getenv("ENV", "UAT").upper() == "UAT" else "prodinfo"
    
    data = {"name": name}
    
    try:
        execute_insert(table_name, data)
        return {"message": f"Name '{name}' added to {table_name}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
