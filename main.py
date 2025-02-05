from fastapi import FastAPI, HTTPException
from database import execute_insert
import os

app = FastAPI()

@app.get("/")
def add_name(name: str = "Jihana"):
    """Inserts a name into the appropriate table."""
    
    # Get the environment variable 'ENV' (no default because it will be set via Docker)
    env = os.getenv("ENV").upper()  # No default, because ENV is guaranteed to be set
    
    # Get schema and table names based on the environment variable
    schema = os.getenv(f"SCHEMA_{env}")  # Default to "uatdata" if not set
    table_name = os.getenv(f"TABLE_{env}")  # Default to "uatinfo" if not set
    
    # Log the environment for debugging
    print(f"Running in {env} environment.")  # This helps you confirm the environment.
    
    data = {"name": name}
    
    try:
        execute_insert(table_name, data, schema)
        return {"message": f"Name '{name}' added to {table_name} in {schema} schema."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
