import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

def listings_encoding(df):

    # 1. Codificar variables categóricas:
    # (a) Label Encoding para binarias
    df['has_availability'] = df['has_availability'].astype(str)
    df['instant_bookable_enc'] = LabelEncoder().fit_transform(df['instant_bookable'])
    df['has_availability_enc'] = LabelEncoder().fit_transform(df['has_availability'])




 
    return df   