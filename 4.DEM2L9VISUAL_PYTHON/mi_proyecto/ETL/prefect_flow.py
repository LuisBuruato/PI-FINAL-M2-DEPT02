from prefect import flow
from extract import extract_usuarios, extract_productos, extract_ordenes, extract_detalle_ordenes, get_engine
from transform import transform_usuarios, transform_productos, transform_ordenes, transform_detalle
from load import load_to_dw
from dbt_tasks import run_dbt

@flow
def ecommerce_etl_dbt_flow():
    engine = get_engine()
