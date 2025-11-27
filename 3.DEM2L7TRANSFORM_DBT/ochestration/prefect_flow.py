# prefect_flow.py
from prefect import flow, task
import sqlalchemy

from extract import extract_data
from load import load_data
from transform import clean_data  # o run_dbt

# Conexión SQL
CONN = "mssql+pyodbc:///?odbc_connect=YOUR_CONNECTION_STRING"

@task
def task_extract(engine):
    return extract_data(engine)

@task
def task_load(data, engine):
    load_data(data, engine)

@task
def task_transform(data):
    return clean_data(data)   # o run_dbt()

@flow(name="ETL_Ecommerce")
def ecommerce_flow():
    engine = sqlalchemy.create_engine(CONN)

    raw = task_extract(engine)
    cleaned = task_transform(raw)
    task_load(cleaned, engine)

    print("Pipeline completado con Prefect!")

if __name__ == "__main__":
    ecommerce_flow()
