

  # ETL
u = load_to_dw(transform_usuarios(extract_usuarios()), 'dim_usuarios', engine)
p = load_to_dw(transform_productos(extract_productos()), 'dim_productos', engine)
o = load_to_dw(transform_ordenes(extract_ordenes()), 'fact_ordenes', engine)
d = load_to_dw(transform_detalle(extract_detalle_ordenes()), 'fact_detalle_ordenes', engine)

# DBT
dbt_output = run_dbt()  # Corre todos los modelos, staging + marts + snapshots
print("DBT run completed")
print(dbt_output)

if __name__ == "__main__":
    ecommerce_etl_dbt_flow()

