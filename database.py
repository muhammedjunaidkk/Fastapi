# database.py
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read the ENV variable (UAT or PROD)
env = os.getenv("ENV", "UAT").upper()  # Default to UAT, and ensure uppercase

# Get the database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Determine the schema based on the environment
schema = "uatdata" if env == "UAT" else "proddata"

# Create the database engine
engine = create_engine(DATABASE_URL)

def execute_insert(table_name: str, data: dict):
    """Generalized function to insert data into a given table."""
    columns = ", ".join(data.keys())
    values = ", ".join([f":{key}" for key in data.keys()])
    
    insert_query = text(f"INSERT INTO {schema}.{table_name} ({columns}) VALUES ({values})")

    try:
        with engine.begin() as connection:
            connection.execute(insert_query, data)
    except Exception as e:
        raise Exception(f"Database Error: {str(e)}")
