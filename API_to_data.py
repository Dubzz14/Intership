import os
import requests
import pandas as pd
from sqlalchemy import create_engine


median = requests.get("https://dummyjson.com/products")

api_dict = median.json()

list_of_records = api_dict.get('products',[])

df_normalized = pd.json_normalize(list_of_records)
df_normalized.columns = df_normalized.columns.str.replace('.', '_', regex=False)
df_normalized.columns = df_normalized.columns.str.replace(':', '_', regex=False)

DB_NAME = os.getenv("DB_NAME", "trial")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "ezeh") 
DB_HOST = os.getenv("DB_HOST", "localhost")

TABLE_NAME = "products_data"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
try:
    engine = create_engine(DATABASE_URL)

    df_normalized.to_sql(
        name=TABLE_NAME, 
        con=engine, 
        if_exists='replace',
        index=False         
    )

    print(f"Success! Data loaded to table: **{TABLE_NAME}** in database **{DB_NAME}**")

except Exception as e:
    print(f"Error loading data to database: Check credentials and PostgreSQL server status. Error: {e}")