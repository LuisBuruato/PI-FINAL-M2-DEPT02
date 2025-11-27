def load_to_dw(df, table_name, engine):
    df.to_sql(table_name, engine, schema='dw', if_exists='replace', index=False)
