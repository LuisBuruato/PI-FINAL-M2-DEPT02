**Resumen del Proyecto de Data Warehouse y ETL para Ecommerce**

---

# 1️⃣ Estructura del Proyecto

- Carpeta principal: `mi_proyecto`
- Subcarpetas:
  - `models/staging`: Contiene los modelos de staging (ej. `stg_usuarios.sql`, `stg_ventas.sql`)
  - `models/marts`: Contiene tablas de hechos y dimensiones finales
  - `snapshots`: Contiene snapshots para manejar Slowly Changing Dimensions (SCD)
  - `macros`: Funciones y macros de DBT
  - `seeds`: Datos de ejemplo (si aplica)

---

# 2️⃣ Modelos DBT

### Staging
- **stg_usuarios**: Limpieza y estandarización de nombres y correos.
- **stg_ventas**: Transformación básica de los datos de ventas.

### Tablas intermedias y finales
- **dim_usuarios**: Dimensión con SCD Tipo 2 para manejar historización.
- **fact_ventas**: Tabla de hechos con cálculo de totales.
- **snapshot_cliente**: Snapshot de `stg_usuarios` para SCD.

### Snapshots
- Implementados con `strategy='check'` y `check_cols` para controlar cambios en las columnas relevantes.
- DBT maneja automáticamente la creación de `dbt_scd_id`, `dbt_valid_from` y `dbt_valid_to`.

---

# 3️⃣ Transformaciones y Limpieza

- Se normalizan nombres y correos de usuarios.
- Se calculan totales y subtotales en tablas de hechos.
- Columnas derivadas manejadas en vistas o tablas finales según requerimientos.
- Implementación de Slowly Changing Dimensions (SCD Tipo 2) usando snapshots.

---

# 4️⃣ Relaciones entre modelos

- Fact tables referencian dimensiones con claves foráneas.
- Dimensiones historizadas (`dim_usuarios`) permiten auditoría y trazabilidad de cambios.
- Índices adicionales para mejorar rendimiento de queries en columnas clave.

---

# 5️⃣ Implementación física en SQL Server

- Creación de tablas de staging (`stg_usuarios`, `stg_ventas`), dimensiones (`dim_usuarios`) y hechos (`fact_ventas`).
- Creación de snapshots (`snapshot_cliente`) para SCD Tipo 2.
- Constraints y llaves foráneas implementadas para garantizar integridad.

---

# 6️⃣ ETL con Python y Prefect

### Conexión a la base de datos
```python
from sqlalchemy import create_engine
from urllib.parse import quote_plus

DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "DESKTOP-JBITTNM\\SQLEXPRESS"
DATABASE = "EcommerceDB"

conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;"
conn_str_quoted = quote_plus(conn_str)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str_quoted}")
```

### Extract
```python
import pandas as pd

def extract_usuarios():
    df = pd.read_sql("SELECT * FROM dbo.Usuarios", engine)
    return df

# Similar para productos, ordenes y detalle
```

### Transform
```python
def transform_usuarios(df):
    df['Nombre'] = df['Nombre'].str.strip().str.title()
    df['Apellido'] = df['Apellido'].str.strip().str.title()
    df['Email'] = df['Email'].str.lower()
    return df
```

### Load
```python
def load_to_dw(df, table_name, engine):
    df.to_sql(table_name, engine, schema='dw', if_exists='replace', index=False)
```

### Prefect Flow
```python
from prefect import flow, task

@task
def etl_usuarios():
    df = extract_usuarios()
    df = transform_usuarios(df)
    load_to_dw(df, 'dim_usuarios', engine)
    return len(df)

@flow
def ecommerce_flow():
    u = etl_usuarios()
    # Similar para productos, ordenes y detalle
```

- ETL completo manejando extracción, transformación y carga en el Data Warehouse.
- Prefect permite orquestación y seguimiento del flujo.

---

# 7️⃣ Consideraciones finales

- DBT se encargó de la transformación de datos y SCD.
- Prefect + Python permite automatizar pipelines ETL para múltiples tablas.
- La integridad de los datos está garantizada mediante claves primarias, foráneas e índices.
- Datos de ejemplo fueron utilizados para pruebas, pero la estructura permite trabajar con datos reales.

