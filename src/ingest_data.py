import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"

def ingest_data() -> pd.DataFrame:
    """Load the retail dataset from the Excel file."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")
    
    try:
        data = pd.read_excel(INPUT_FILE)
    except Exception as e:
        raise ValueError(f"Error reading input file: {e}")

    return data


def main() -> None:
    """Load the retail dataset and display the available columns."""
    data = ingest_data()
    print("Available rows:", len(data))

if __name__ == "__main__":
    main()    
    
