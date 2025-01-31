from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()  

app = FastAPI()

# Read the ENV variable (UAT or PROD)
env = os.getenv("ENV", "UAT").upper()  # Default to UAT, and ensure uppercase

# Get the database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Determine the schema and table based on the environment
schema = "uatdata" if env == "UAT" else "proddata"
table_name = "uatinfo" if env == "UAT" else "prodinfo"

# Create the database engine
engine = create_engine(DATABASE_URL)

@app.get("/")
def insert_name(name: str = "Default Name"):
    """Inserts a name into the appropriate schema and table."""
    insert_query = text(f"INSERT INTO {schema}.{table_name} (name) VALUES (:name)")

    try:
        with engine.begin() as connection:  # Use `begin()` for transactions
            connection.execute(insert_query, {"name": name})

        return {"message": f"Name '{name}' added to {schema}.{table_name}."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database Error: {str(e)}")      
