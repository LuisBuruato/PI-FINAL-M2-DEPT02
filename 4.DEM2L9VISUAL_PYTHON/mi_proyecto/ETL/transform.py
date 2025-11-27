from prefect import task

@task
def transform_usuarios(df):
    df['nombre_usuario'] = df['nombre_usuario'].str.strip().str.title()
    df['email_usuario'] = df['email_usuario'].str.lower()
    return df

@task
def transform_productos(df):
    df['nombre_producto'] = df['nombre_producto'].str.strip().str.title()
    return df

@task
def transform_ordenes(df):
    return df

@task
def transform_detalle(df):
    df['subtotal'] = df['cantidad'] * df['precio_unitario']
    return df


from sqlalchemy import create_engine

def load_to_dw(df, table_name, engine):
    df.to_sql(table_name, engine, schema='dbo', if_exists='replace', index=False)
