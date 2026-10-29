"""Display a sample and schema overview of the retail dataset."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"


def main() -> None:
    """Load the retail dataset and display its basic structure."""
    data = pd.read_excel(INPUT_FILE)

    print(data.head())
    print(data.shape)
    print(data.columns)
    print(data.dtypes)


if __name__ == "__main__":
    main()
