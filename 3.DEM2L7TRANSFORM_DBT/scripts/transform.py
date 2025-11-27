# transform.py

def clean_usuarios(df):
    df["Email"] = df["Email"].str.lower()
    df["NombreCompleto"] = df["Nombre"] + " " + df["Apellido"]
    return df

def clean_data(data: dict):
    data["usuarios"] = clean_usuarios(data["usuarios"])
    return data
