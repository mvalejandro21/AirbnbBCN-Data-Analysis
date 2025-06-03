

def remove_duplicates(df):
   
    print("🔍 [INFO] Eliminando duplicados...")
    n_dup = df.duplicated().sum()
    if n_dup == 0:
        print("✅ [SUCCESS] No se encontraron duplicados.")
        return df
    else:
        print(f"🔍 [INFO] Filas duplicadas: {n_dup} \n Filas antes de la limpieza: {df.shape[0]}")
        df = df.drop_duplicates()
        print(f"✅ [SUCCESS] Duplicados eliminados. Filas restantes: {df.shape[0]}")
        return df