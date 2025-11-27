from prefect import flow, task
from extract import extract_usuarios, extract_productos, extract_ordenes, extract_detalle_ordenes
from transform import transform_usuarios, transform_productos, transform_ordenes, transform_detalle
from load import load_to_dw
from extract import get_engine

@task
def etl_usuarios():
    df = extract_usuarios()
    df = transform_usuarios(df)
    engine = get_engine()
    load_to_dw(df, 'dim_usuarios', engine)
    return len(df)

@task
def etl_productos():
    df = extract_productos()
    df = transform_productos(df)
    engine = get_engine()
    load_to_dw(df, 'dim_productos', engine)
    return len(df)

@task
def etl_ordenes():
    df = extract_ordenes()
    df = transform_ordenes(df)
    engine = get_engine()
    load_to_dw(df, 'fact_ordenes', engine)
    return len(df)

@task
def etl_detalle():
    df = extract_detalle_ordenes()
    df = transform_detalle(df)
    engine = get_engine()
    load_to_dw(df, 'fact_detalle_ordenes', engine)
    return len(df)

@flow
def ecommerce_flow():
    u = etl_usuarios()
    p = etl_productos()
    o = etl_ordenes()
    d = etl_detalle()
    print(f"Usuarios: {u}, Productos: {p}, Ordenes: {o}, Detalle: {d}")

if __name__ == "__main__":
    ecommerce_flow()



