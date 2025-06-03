import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def handle_nulls(df):
    """
    This function handles null values in the DataFrame.
    It fills null values in the 'description' column with a placeholder.
    """
    print("🔍 [INFO] Manejo de valores nulos...")

    """df = fill_description(df)"""
    df = fill_bathrooms(df)

    df = fill_beds_bedrooms(df)

    df = fill_price(df)

    df = fill_availability(df)

    df = fill_revenue_l365d(df)

    df = handle_review_columns(df)

    df = handle_superhost(df)

    print("✅ [SUCCESS] Manejo de valores nulos completado.")

    # Imprimir columnas con valores nulos
    null_columns = df.columns[df.isnull().any()].tolist()
    if null_columns:
        print("🧾 [INFO] Columnas con valores nulos después del manejo:")
        print(null_columns)
    else:
        print("✅ [SUCCESS] No quedan valores nulos en el DataFrame.")



    
    
    return df



"""
 LA COLUMNA DESCRIPTION NO SE UTILIZA EN EL MODELO FINAL, PERO SE MANTIENE POR SI SE NECESITA EN EL FUTURO.

def fill_description(df):
    
    Fill null values in the 'description' column with a placeholder.
    
    print("🔍 [INFO] Llenando valores nulos en la columna 'description'...")

    # Placeholder for missing descriptions
    placeholder = "No description available"

    # Fill null values in the 'description' column
    df['description'] = df['description'].fillna(placeholder)

    print("✅ [SUCCESS] Valores nulos en 'description' llenados.")
    return df
"""

def fill_bathrooms(df):
    """
    Fill missing values in the 'bathrooms' column based on the 'bathrooms_text' column.
    If 'bathrooms' is NaN, it will check 'bathrooms_text' for a corresponding value.
    If 'bathrooms_text' is also NaN or does not match any known values, it will fill with the median of the column.
    """ 
    # Diccionario de mapeo de texto a valor numérico
    text_to_num = {
        '1 bath': 1.0, '2 baths': 2.0, '1 shared bath': 1.0, '1 private bath': 1.0,
        '1.5 baths': 1.5, '2 shared baths': 2.0, 'Shared half‑bath': 0.5, 'Half‑bath': 0.5,
        # … incluye aquí todos los casos relevantes …
    }

    def fill_bath_from_text(row):
        # Si 'bathrooms' ya tiene valor, lo devolvemos tal cual
        if not np.isnan(row['bathrooms']):
            return row['bathrooms']
        # Si está vacío pero hay texto en 'bathrooms_text' y coincide en el diccionario
        txt = row['bathrooms_text']
        if isinstance(txt, str) and txt in text_to_num:
            return text_to_num[txt]
        # En caso contrario, devolvemos NaN para imputar luego con la media
        return np.nan

    # 1) Aplicar la función fila a fila
    df['bathrooms'] = df.apply(fill_bath_from_text, axis=1)  # :contentReference[oaicite:0]{index=0}

    # 2) Rellenar los NaN restantes con la mediana
    median_baths = df['bathrooms'].median()
    print(f"🔍 [INFO] Imputando 'bathrooms' con la mediana: {median_baths}")
    df['bathrooms'] = df['bathrooms'].fillna(median_baths) 
    print("✅ [SUCCESS] Valores nulos en 'bathrooms' llenados.")
    df.drop(columns=['bathrooms_text'], inplace=True, errors='ignore')  # Eliminar la columna de texto si existe

    print("🧾 [INFO] Recuento de valores individuales de bathrooms:"  )
    print(df['bathrooms'].value_counts(dropna=False))
    df['bathrooms'] = df['bathrooms'].astype(float)
    # Imprimir el recuento de valores únicos
    print("🧾 [INFO] Recuento de valores únicos de bathrooms:", df['bathrooms'].nunique())
    return df

def fill_beds_bedrooms(df):
    """
    Fill missing values in the 'beds' and 'bedrooms' columns using Iterative Imputer.
    This method uses the other columns to predict the missing values.
    """
    print("🔍 [INFO] Llenando valores nulos en las columnas 'beds' y 'bedrooms'...")
    cols = ['beds', 'bedrooms','accommodates','bathrooms']

    X = df[cols].copy()

    imp = IterativeImputer(
        estimator=None,           # Usa BayesianRidge por defecto
        max_iter=10,
        random_state=42,
        sample_posterior=True     # Simula múltiples imputaciones
    )


    # Ajustar e imputar  
    X_imputed = imp.fit_transform(X)

    # Reemplazar las columnas imputadas
    df['bedrooms'] = X_imputed[:, 0]
    df['beds'] = X_imputed[:, 1]

    # Convertir a tipo entero
    df['bedrooms'] = df['bedrooms'].round().astype('Int64')
    df['beds'] = df['beds'].round().astype('Int64')

    # Reemplazar los NaN restantes con la mediana
    median_beds = df['beds'].median()
    df['beds'] = df['beds'].fillna(median_beds)
    median_bedrooms = df['bedrooms'].median()
    df['bedrooms'] = df['bedrooms'].fillna(median_bedrooms)

    print("✅ [SUCCESS] Valores nulos en 'beds' y 'bedrooms' llenados.")
    return df


from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import numpy as np

def fill_availability(df):
    """
    Fill missing values in the 'has_availability' column with false.
    """

    
    print("🔍 [INFO] Llenando valores nulos en la columna 'has_availability'...")

    df['has_availability_was_missing'] = df['has_availability'].isna().astype(int)
    df["has_availability"] = df["has_availability"].fillna(False)

    return df


def fill_price(df):
    """
    Imputa los valores faltantes en 'price'.
    - Si la fila indica un anuncio inactivo (sin disponibilidad), se imputa con 0.
    - El resto se imputa usando MICE (IterativeImputer).
    - Se crea un flag 'price_was_missing' en todas las filas originalmente nulas.
    """

    print("🔍 [INFO] Imputando valores faltantes en 'price'...")

    # 1. Convertir 'price' a float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # 2. Flag en todos los NaN (antes de imputar)
    df['price_was_missing'] = df['price'].isna().astype(int)

    # 3. Detectar anuncios cerrados (sin disponibilidad)
    closed_mask = (df['has_availability'] == False) | (df['availability_365'] == 0)

    # 4. Imputar 0 en los anuncios cerrados que tengan price NaN
    df.loc[closed_mask & df['price'].isna(), 'price'] = 0.0

    # 5. Imputar el resto de los NaN con MICE
    cols = ['price', 'bedrooms', 'beds', 'accommodates', 'bathrooms']
    X = df[cols]

    imp = IterativeImputer(
        estimator=None,
        max_iter=10,
        sample_posterior=True,
        random_state=0
    )

    # 6. Ajustar e imputar
    X_imputed = imp.fit_transform(X)

    # 7. Reemplazar solo la columna 'price'
    df['price'] = X_imputed[:, 0]

    print("✅ [SUCCESS] 'price' imputado (0 si cerrado, MICE si MAR).")
    return df




def fill_revenue_l365d(df):
    """
    Imputa los valores faltantes en 'estimated_revenue_l365d'.
    - Si la fila indica un anuncio cerrado (sin disponibilidad), se imputa con 0.
    - El resto se imputa usando IterativeImputer (MICE).
    - Se crea un flag 'revenue_was_missing' para todas las filas originalmente nulas.
    """

    print("🔍 [INFO] Imputando valores faltantes en 'estimated_revenue_l365d'...")

    # 1. Asegurar que la columna sea float
    df['estimated_revenue_l365d'] = df['estimated_revenue_l365d'].replace('[\$,]', '', regex=True).astype(float)

    # 2. Flag para todos los valores originalmente nulos
    df['revenue_was_missing'] = df['estimated_revenue_l365d'].isna().astype(int)

    # 3. Máscara de listados cerrados
    closed_mask = (df['has_availability'] == False) | (df['availability_365'] == 0)

    # 4. Imputar 0 en esos casos si hay NaN
    df.loc[closed_mask & df['estimated_revenue_l365d'].isna(), 'estimated_revenue_l365d'] = 0.0

    # 5. Imputación multivariante (MICE) para el resto
    cols = ['estimated_revenue_l365d', 'price', 'bedrooms', 'beds', 'accommodates', 'bathrooms']
    X = df[cols]

    imp = IterativeImputer(
        estimator=None,
        max_iter=10,
        sample_posterior=True,
        random_state=0
    )

    # 6. Imputar
    X_imputed = imp.fit_transform(X)

    # 7. Reemplazar solo la columna de revenue
    df['estimated_revenue_l365d'] = X_imputed[:, 0]

    print("✅ [SUCCESS] 'estimated_revenue_l365d' imputado (0 si cerrado, MICE si MAR).")
    return df


def handle_review_columns(df):
    """
    Imputa y normaliza las columnas relacionadas con reseñas en un dataset de Airbnb.
    - Imputa 0 en contadores cuando no hay reviews.
    - Crea una flag binaria 'has_reviews'.
    - Preserva NaN en columnas de puntaje si no hay reviews.
    """

    print("🔍 [INFO] Tratando columnas de reseñas...")

    # 1. Imputar 0 donde tiene sentido (recuento de reviews)
    review_count_cols = [
        'number_of_reviews',
        'number_of_reviews_ltm',
        'number_of_reviews_l30d',
        'reviews_per_month'
    ]
    
    for col in review_count_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # 2. Crear flag binaria has_reviews
    if 'number_of_reviews' in df.columns:
        df['has_reviews'] = (df['number_of_reviews'] > 0).astype(int)

    # 3. Revisar columnas de puntajes
    review_score_cols = [
        'review_scores_rating',
        'review_scores_accuracy',
        'review_scores_cleanliness',
        'review_scores_checkin',
        'review_scores_communication',
        'review_scores_location',
        'review_scores_value'
    ]

    for col in review_score_cols:
        if col in df.columns:
            # Si no hay reviews, forzar a NaN
            df.loc[df['has_reviews'] == 0, col] = np.nan
            # Opcional: podrías imputar la media para los que sí tienen reviews (no recomendado si hay pocos nulos)

    print("✅ [SUCCESS] Columnas de reseñas tratadas correctamente.")
    return df



def handle_superhost(df):
    """
    Imputa los valores faltantes en la columna 'host_is_superhost' con 'False'.
    """
    df['host_is_superhost'] = df['host_is_superhost'].fillna(False)
    print("✅ [SUCCESS] 'host_is_superhost' imputado con False.")
    return df
