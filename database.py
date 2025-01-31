from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)

def execute_insert(table_name: str, data: dict, schema: str):
    """Generalized function to insert data into a given table with schema."""
    columns = ", ".join(data.keys())
    values = ", ".join([f":{key}" for key in data.keys()])
    
    # Use the schema passed as a parameter
    insert_query = text(f"INSERT INTO {schema}.{table_name} ({columns}) VALUES ({values})")

    try:
        with engine.begin() as connection:
            connection.execute(insert_query, data)
    except Exception as e:
        raise Exception(f"Database Error: {str(e)}")
