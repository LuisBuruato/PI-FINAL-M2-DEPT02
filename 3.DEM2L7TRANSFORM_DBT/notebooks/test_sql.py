import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Configuración
DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "DESKTOP-JBITTNM\\SQLEXPRESS"  # Tu instancia
DATABASE = "EcommerceDB"                 # Base de datos real

# Cadena de conexión con Trusted Connection
conn_str = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;"
conn_str_quoted = quote_plus(conn_str)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str_quoted}")

# Probar consulta simple
df = pd.read_sql("SELECT TOP 5 * FROM dbo.Usuarios", engine)
print(df)



