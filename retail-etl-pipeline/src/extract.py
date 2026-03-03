import pandas as pd

def extract_data():
    file_path = "data/raw_sales.csv"
    df = pd.read_csv(file_path)
    return df