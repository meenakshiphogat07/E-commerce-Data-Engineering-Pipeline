import pandas as pd
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingest_data() -> pd.DataFrame:
    """Load the retail dataset from the Excel file."""
def ingest_data() -> pd.DataFrame:
    """Load the retail dataset from the Excel file."""

    logging.info("Data ingestion started.")

    if not INPUT_FILE.exists():
        logging.error(f"Input file not found: {INPUT_FILE}")
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    logging.info("Input file found successfully.")

    try:
        data = pd.read_excel(INPUT_FILE)

        logging.info(
            f"Data loaded successfully: {len(data)} rows "
            f"and {len(data.columns)} columns."
        )

        return data

    except Exception as e:
        logging.exception("Error occurred during data ingestion.")
        raise ValueError(f"Error reading input file: {e}") from e

    return data


def main() -> None:
    """Load the retail dataset and display the available columns."""
    data = ingest_data()
    print("Available rows:", len(data))
    print("Available columns:", list(data.columns))

if __name__ == "__main__":
    main()    
    
