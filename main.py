from fastapi import FastAPI, HTTPException
from database import execute_insert
import os

app = FastAPI()

@app.get("/")
def add_name(name: str = "AMAL"):
    """Inserts a name into the appropriate table."""
    
    # Get the environment variable 'ENV' (defaults to "UAT" if not set)
    env = os.getenv("ENV", "UAT").upper()
    
    # Log the environment for debugging
    print(f"Running in {env} environment.")  # This helps you confirm the environment.
    
    # Set the appropriate table name based on the environment
    table_name = "uatinfo" if env == "UAT" else "prodinfo"
    
    data = {"name": name}
    
    try:
        execute_insert(table_name, data)
        return {"message": f"Name '{name}' added to {table_name}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
