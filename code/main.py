from Dataset_Cleaning.cleaning_data  import data_cleaning
from Dataset_Cleaning.cleaning_data  import load_data

if __name__ == "__main__":
    
    df = load_data()

    data_cleaning(df)

    