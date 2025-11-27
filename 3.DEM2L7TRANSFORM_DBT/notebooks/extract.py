import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def get_engine():
    DRIVER = "ODBC Driver 17 for SQL Server"
    SERVER = "DESKTOP-JBITTNM\\SQLEXPRESS"
    DATABASE = "EcommerceDB"

    conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;"
    conn_str_quoted = quote_plus(conn_str)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str_quoted}")
    return engine

def extract_usuarios():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM dbo.Usuarios", engine)
    return df

def extract_productos():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM dbo.Productos", engine)
    return df

def extract_ordenes():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM dbo.Ordenes", engine)
    return df

def extract_detalle_ordenes():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM dbo.DetalleOrdenes", engine)
    return df

