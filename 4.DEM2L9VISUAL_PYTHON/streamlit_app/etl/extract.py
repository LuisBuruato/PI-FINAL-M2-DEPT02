from sqlalchemy import create_engine

def get_engine():
    """
    Devuelve un engine SQLAlchemy conectado a tu base de datos SQL Server
    """
    server = "localhost\\SQLEXPRESS"  # Cambia si tu servidor es otro
    database = "EcommerceDB"          # Nombre correcto de tu base de datos
    driver = "ODBC Driver 17 for SQL Server"

    connection_string = (
        f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
    )
    engine = create_engine(connection_string)
    return engine

