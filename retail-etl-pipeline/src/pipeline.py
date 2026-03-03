import logging
import os
from extract import extract_data
from transform import transform_data
from load import load_data

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    try:
        logging.info("Pipeline started")

        df = extract_data()
        logging.info("Data extracted")

        df_transformed = transform_data(df)
        logging.info("Data transformed")

        load_data(df_transformed)
        logging.info("Data loaded into database")

        logging.info("Pipeline finished successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
    