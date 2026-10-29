"""Remove duplicate rows and records without a product description."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with duplicate rows and missing descriptions removed."""
    cleaned_data = data.drop_duplicates()
    return cleaned_data.dropna(subset=["Description"])


def main() -> None:
    """Load the retail data, clean it, and report the existing checks."""
    data = pd.read_excel(INPUT_FILE)
    cleaned_data = clean_data(data)

    print(f"Rows before cleaning: {len(data)}")
    print(f"Rows after cleaning: {len(cleaned_data)}")
    print(
        "Rows with missing customer IDs after cleaning: "
        f"{cleaned_data['CustomerID'].isna().sum()}"
    )


if __name__ == "__main__":
    main()
