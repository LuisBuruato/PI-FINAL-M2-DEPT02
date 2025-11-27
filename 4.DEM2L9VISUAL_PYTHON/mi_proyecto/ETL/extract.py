from sqlalchemy import create_engine

def get_engine():
    server = "DESKTOP-JBITTNM\\SQLEXPRESS"
    database = "EcommerceDB"  # <- nombre correcto de tu base de datos
    driver = "ODBC Driver 17 for SQL Server"

    # Conexión con Windows Authentication
    connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"

    engine = create_engine(connection_string)
    return engine















