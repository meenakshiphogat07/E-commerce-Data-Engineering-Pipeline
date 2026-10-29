"""Report basic completeness and consistency metrics for the retail data."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"


def main() -> None:
    """Load the dataset and print the existing data quality checks."""
    data = pd.read_excel(INPUT_FILE)

    print(data.isna().sum())
    print(data.duplicated().sum())
    print(data.loc[data["Quantity"] < 0].shape[0])
    print(data.loc[data["UnitPrice"] == 0].shape[0])
    print(data["Country"].nunique())


if __name__ == "__main__":
    main()
