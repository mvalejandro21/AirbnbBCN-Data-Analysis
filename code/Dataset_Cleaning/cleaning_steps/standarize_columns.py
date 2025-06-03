def standardize_column_names(df):
   
    df.columns = (
        df.columns
        .str.strip()               # elimina espacios al inicio/fin
        .str.lower()               # convierte a minúsculas
        .str.replace(" ", "_")     # reemplaza espacios por guiones bajos
        .str.replace(r"[^\w_]", "", regex=True)  # quita símbolos raros
    )

    print("🧾 [COLUMNS] Nombres de columnas estandarizados.")
    print("🧾 [INFO] Columnas actuales en el dataset:"
          f"\n{df.columns.tolist()}")
    

    return df
