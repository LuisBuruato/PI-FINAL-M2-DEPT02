def transform_usuarios(df):
    # Ejemplo: limpiar nombres y correos
    df['Nombre'] = df['Nombre'].str.strip().str.title()
    df['Apellido'] = df['Apellido'].str.strip().str.title()
    df['Email'] = df['Email'].str.lower()
    return df

def transform_productos(df):
    df['Nombre'] = df['Nombre'].str.strip().str.title()
    return df

def transform_ordenes(df):
    # Puedes agregar transformaciones de fechas, montos, etc.
    return df

def transform_detalle(df):
    df['Subtotal'] = df['Cantidad'] * df['PrecioUnitario']
    return df
