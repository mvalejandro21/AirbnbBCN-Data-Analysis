def drop_irrelevant_columns(df):
   

    #print("🧾 [INFO] Columnas actuales en el dataset:")


    # Detectar columnas vacías
    empty_cols = df.columns[df.isnull().all()].tolist()
    if empty_cols:
        print("🧾 [INFO] Columnas vacías detectadas:")
        print(empty_cols)   

    # Detectar columnas constantes
    constant_cols = df.columns[df.nunique() <= 1].tolist()
    if constant_cols:
        print("🧾 [INFO] Columnas constantes detectadas:")
        print(constant_cols)

    # Lista manual de columnas que no queremos usar
    manual_drop = ["listing_id,",   "neighbourhood_group", "last_review", "scrape_id", "last_scraped",
                    "summary", "space", "description", "experiences_offered", "neighborhood_overview", "notes", "transit", "access", "interaction",
                      "house_rules", "thumbnail_url", "medium_url", "picture_url", "xl_picture_url", "host_url", "host_since", "host_location", "host_about", "host_response_time",
                      "host_response_rate", "host_acceptance_rate", "host_thumbnail_url", "host_picture_url", "host_neighbourhood", "host_verifications",
                      "calendar_last_scraped", "calendar_updated", "first_review","last_review", "license", "neighbourhood", "license",  
                      "host_has_profile_pic", "host_identity_verified", "minimum",'minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'minimum_nights_avg_ntm', 
                      'maximum_nights_avg_ntm',  'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 
                      'review_scores_location', 'review_scores_value']

    cols_to_drop = list(set(empty_cols + constant_cols + manual_drop))

    # Filtramos solo las columnas que realmente existen en el DataFrame
    real_cols = [col for col in cols_to_drop if col in df.columns]

    # Eliminamos las columnas existentes
    df = df.drop(columns=real_cols, errors="ignore")

    print("🧾 [INFO] Columnas a eliminar:")
    print(cols_to_drop)
    #print("🧾 [INFO] Columnas restantes después de la limpieza:"
    #      f"\n{df.columns.tolist()}")
    print("✅ [SUCCESS] Columnas irrelevantes eliminadas.")

    return df

