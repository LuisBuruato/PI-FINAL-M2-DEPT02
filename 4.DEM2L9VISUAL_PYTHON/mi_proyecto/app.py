# etl_pipeline.py
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from prefect import flow, task

# ----------------------------------------
# 1️⃣ Conexión a SQL Server
# ----------------------------------------
DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "DESKTOP-JBITTNM\\SQLEXPRESS"
DATABASE = "EcommerceDB"

conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;"
conn_str_quoted = quote_plus(conn_str)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str_quoted}")

# ----------------------------------------
# 2️⃣ Tareas de Extracción
# ----------------------------------------
@task
def extract_usuarios():
    return pd.read_sql("SELECT * FROM dbo.Usuarios", engine)

@task
def extract_productos():
    return pd.read_sql("SELECT * FROM dbo.Productos", engine)

@task
def extract_ordenes():
    return pd.read_sql("SELECT * FROM dbo.Ordenes", engine)

@task
def extract_detalle():
    return pd.read_sql("SELECT * FROM dbo.DetalleOrdenes", engine)

# ----------------------------------------
# 3️⃣ Tareas de Transformación
# ----------------------------------------
from prefect import task

@task
def transform_usuarios(df):
    if 'nombre_usuario' in df.columns:
        df['nombre_usuario'] = df['nombre_usuario'].str.strip().str.title()
    if 'email_usuario' in df.columns:
        df['email_usuario'] = df['email_usuario'].str.strip().str.lower()
    return df

@task
def transform_productos(df):
    if 'nombre_producto' in df.columns:
        df['nombre_producto'] = df['nombre_producto'].str.strip().str.title()
    return df

@task
def transform_ordenes(df):
    # Transformaciones opcionales
    return df

@task
def transform_detalle(df):
    if 'cantidad' in df.columns and 'precio_unitario' in df.columns:
        df['subtotal'] = df['cantidad'] * df['precio_unitario']
    return df


# ----------------------------------------
# 4️⃣ Carga a DW
# ----------------------------------------
@task
def load_to_dw(df, table_name):
    df.to_sql(table_name, engine, schema='dbo', if_exists='replace', index=False)
    return len(df)

# ----------------------------------------
# 5️⃣ Flujo ETL
# ----------------------------------------
@flow
def ecommerce_etl_flow():
    # Usuarios
    usuarios_raw = extract_usuarios()
    usuarios_clean = transform_usuarios(usuarios_raw)
    count_usuarios = load_to_dw(usuarios_clean, 'dim_usuarios')

    # Productos
    productos_raw = extract_productos()
    productos_clean = transform_productos(productos_raw)
    count_productos = load_to_dw(productos_clean, 'dim_productos')

    # Ordenes
    ordenes_raw = extract_ordenes()
    ordenes_clean = transform_ordenes(ordenes_raw)
    count_ordenes = load_to_dw(ordenes_clean, 'fact_ordenes')

    # Detalle Ordenes
    detalle_raw = extract_detalle()
    detalle_clean = transform_detalle(detalle_raw)
    count_detalle = load_to_dw(detalle_clean, 'fact_detalle_ordenes')

    print(f"Usuarios cargados: {count_usuarios}")
    print(f"Productos cargados: {count_productos}")
    print(f"Ordenes cargadas: {count_ordenes}")
    print(f"Detalle de ordenes cargadas: {count_detalle}")

# ----------------------------------------
# 6️⃣ Ejecutar el flujo
# ----------------------------------------
if __name__ == "__main__":
    ecommerce_etl_flow()

