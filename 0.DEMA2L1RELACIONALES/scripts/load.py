\
       """
Load step: cargar CSVs de staging a la base de datos Postgres
Crea los esquemas 'staging', 'raw' y 'marts' si no existen.
Configura la variable de entorno DB_URI o edita la línea de abajo.
"""

import os
import pandas as pd
from sqlalchemy import create_engine, text

# ---------------------------------------------
# 1. Configurar conexión a DB
# ---------------------------------------------
DB_URI = os.getenv('DB_URI', 'postgresql://postgres:postgres@localhost:5432/ecommerce')
engine = create_engine(DB_URI, echo=False)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STAGING_DIR = os.path.join(BASE_DIR, 'data', 'staging')

# ---------------------------------------------
# 2. Crear esquemas si no existen
# ---------------------------------------------
with engine.begin() as conn:  # begin() maneja commit/rollback automáticamente
    for schema in ['raw', 'staging', 'marts']:
        conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS {schema}'))
        print(f"[INFO] Schema '{schema}' asegurado.")

# ---------------------------------------------
# 3. Función helper para cargar CSV a Postgres
# ---------------------------------------------
def write_table(csv_path, schema, table_name):
    try:
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, con=engine, schema=schema, if_exists='replace', index=False)
        print(f"[OK] {schema}.{table_name} ({len(df)} filas)")
    except Exception as e:
        print(f"[ERROR] No se pudo cargar {table_name}: {e}")

# ---------------------------------------------
# 4. Cargar todos los archivos staging
# ---------------------------------------------
staging_files = [f for f in os.listdir(STAGING_DIR) if f.st_]()_
