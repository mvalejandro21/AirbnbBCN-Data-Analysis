import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 



def handle_outliers(df, multiplier=1.5, use_percentile=True):
    """
    - Cap valores extremos no realistas (por percentil 99 o IQR).
    - Fuerza mínimo a 0 si hay valores negativos.
    - Añade flags de outliers válidos.

    Parámetros:
        df (pd.DataFrame): Dataset original
        multiplier (float): Multiplicador de IQR (si use_percentile=False)
        use_percentile (bool): Si True, usa percentiles 1-99

    Retorna:
        pd.DataFrame: Dataset procesado con capping y flags
    """
    df = df.copy()

    # Columnas a capar dinámicamente
    cap_columns = ['beds', 'bedrooms', 'bathrooms', 'price', 'estimated_revenue_l365d']
    for col in cap_columns:
        if col in df.columns:
            if use_percentile:
                lower, upper = df[col].quantile([0.01, 0.99])
            else:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - multiplier * IQR
                upper = Q3 + multiplier * IQR

            lower = max(lower, 0)  # Forzar mínimo 0
            df[col] = df[col].clip(lower=lower, upper=upper)
            print(f"✂️  '{col}' capado entre {round(lower, 2)} y {round(upper, 2)}")

    # Columnas donde se permiten outliers, pero se marcan
    flag_columns = ['number_of_reviews', 'accommodates']
    for col in flag_columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - multiplier * IQR
            upper = Q3 + multiplier * IQR
            flag_col = f'is_outlier_{col}'
            df[flag_col] = ((df[col] < lower) | (df[col] > upper)).astype(int)
            print(f"📍 Flag '{flag_col}' añadido: {df[flag_col].sum()} registros")

    print("✅ [SUCCESS] Outliers gestionados correctamente.")
    return df


