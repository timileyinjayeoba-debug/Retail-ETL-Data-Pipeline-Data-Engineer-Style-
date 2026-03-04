import pandas as pd
from pathlib import Path


def extract_data():
    # Get project root directory (retail-etl-pipeline/)
    base_dir = Path(__file__).resolve().parent.parent
    
    # Build full path to CSV
    file_path = base_dir / "data" / "raw_sales.csv"
    
    # Read file
    df = pd.read_csv(file_path)
    
    # return df