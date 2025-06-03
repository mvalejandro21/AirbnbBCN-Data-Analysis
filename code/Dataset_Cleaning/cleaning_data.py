import pandas as pd
from .cleaning_steps.remove_duplicates import remove_duplicates
from .cleaning_steps.standarize_columns import standardize_column_names
from .cleaning_steps.drop_irrelevant_columns import drop_irrelevant_columns
from .cleaning_steps.handle_nulls import handle_nulls
from .cleaning_steps.encoding import listings_encoding
from .cleaning_steps.handle_outliers import handle_outliers

def load_data():

    
    try:
        df = pd.read_csv("data/listings.csv", encoding='utf-8')

        if df.empty or df.shape[1] == 0:
            print("⚠️ [WARNING] CSV cargado pero está vacío o sin columnas.")
            return None

        print(f"✅ [SUCCESS] Datos cargados correctamente: {df.shape[0]} filas, {df.shape[1]} columnas.")
        return df

    except FileNotFoundError:
        print("❌ [ERROR] Archivo CSV no encontrado en la ruta especificada.")
        return None

    except pd.errors.ParserError:
        print("❌ [ERROR] Fallo al parsear el archivo CSV. ¿Está bien formado?")
        return None

    except Exception as e:
        print(f"❌ [ERROR] Error inesperado al cargar el CSV: {e}")
        return None

def save_data(df):
    print(df['bathrooms'].value_counts(dropna=False))


    try:
        df.to_csv("data/cleaned_listings.csv", index=False, encoding='utf-8', decimal=',')
        print("✅ [SUCCESS] Datos guardados correctamente en 'data/cleaned_listings.csv'.")
    except Exception as e:
        print(f"❌ [ERROR] Error al guardar el archivo CSV: {e}")

def data_cleaning(df):

    print("🔍 [INFO] Iniciando limpieza de datos...")
    df = remove_duplicates(df)

    df = standardize_column_names(df)

    df = drop_irrelevant_columns(df)

    df = handle_nulls(df)
    
    df = listings_encoding(df)

    df = handle_outliers(df)

    save_data(df)

    return df


    


