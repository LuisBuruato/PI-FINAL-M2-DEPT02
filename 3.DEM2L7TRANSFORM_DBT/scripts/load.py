# load.py
import pandas as pd

def load_dataframe(df: pd.DataFrame, table_name: str, engine, schema="staging"):
    df.to_sql(
        table_name,
        engine,
        schema=schema,
        if_exists="replace",  # o "append"
        index=False
    )
    print(f"Cargado: {schema}.{table_name}")

def load_data(data: dict, engine):
    for name, df in data.items():
        load_dataframe(df, name, engine)
