import pandas as pd
from ..utils.normalize_columns import normalize_columns
        

def csv_reader(file_path: str):
    try:
        if file_path:
            df = pd.read_csv(file_path)
            df_nomralized= normalize_columns(df)

            return df_nomralized
            
    except FileNotFoundError:
        print("Error: File Not found error.")