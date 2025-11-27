# extract.py
import pandas as pd
import sqlalchemy

def extract_usuarios(engine):
    query = "SELECT * FROM dbo.Usuarios"
    return pd.read_sql(query, engine)

def extract_productos(engine):
    query = "SELECT * FROM dbo.Productos"
    return pd.read_sql(query, engine)

def extract_ordenes(engine):
    query = "SELECT * FROM dbo.Ordenes"
    return pd.read_sql(query, engine)

def extract_data(engine):
    data = {
        "usuarios": extract_usuarios(engine),
        "productos": extract_productos(engine),
        "ordenes": extract_ordenes(engine),
    }
    return data
