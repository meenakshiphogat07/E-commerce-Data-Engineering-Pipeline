"""Display the columns available in the retail dataset."""

from pathlib import Path
from clean_data import clean_data

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"


def main() -> None:
    """Load the retail dataset and display its column names."""
    data = pd.read_excel(INPUT_FILE)
    print(data.columns)
    cleaned_data=clean_data(data)
    print(cleaned_data.duplicated().sum())
    print(cleaned_data[cleaned_data['UnitPrice']<0].shape[0])
    print(cleaned_data[cleaned_data['Quantity']==0].shape[0])
    if cleaned_data.duplicated().sum()>0:
        print("Validation failed")
    else:
        print("Validation passed")    




if __name__ == "__main__":
    main()
