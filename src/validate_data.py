"""Display the columns available in the retail dataset."""

from pathlib import Path
from clean_data import clean_data

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"

def validate_data(data: pd.DataFrame) -> None:
    """Perform data quality checks on the cleaned dataset."""
    duplicate_count = data.duplicated().sum()
    missing_description_count = data['Description'].isna().sum()
    missing_invoice_count = data['InvoiceNo'].isna().sum()
    negative_price_count = (data[data['UnitPrice'] < 0].shape[0])
    zero_quantity_count = (data[data['Quantity'] == 0].shape[0])

    print("\nData Quality Report")
    print("-------------------")
    print("Duplicate records:", duplicate_count)
    print("Negative prices:", negative_price_count)
    print("Zero quantities:", zero_quantity_count)

    if (duplicate_count == 0
            and negative_price_count == 0
            and zero_quantity_count == 0):
        print("\nValidation passed")
    else:
        print("\nValidation failed")


def main() -> None:
    """Load the retail dataset and validate data quality."""

    data = pd.read_excel(INPUT_FILE)

    print("Available columns:")
    print(data.columns)

    cleaned_data = clean_data(data)

    # Data quality checks
    duplicate_count = cleaned_data.duplicated().sum()

    negative_price_count = (
        cleaned_data[cleaned_data['UnitPrice'] < 0].shape[0]
    )

    zero_quantity_count = (
        cleaned_data[cleaned_data['Quantity'] == 0].shape[0]
    )

    # Display validation results
    print("\nData Quality Report")
    print("-------------------")
    print("Duplicate records:", duplicate_count)
    print("Negative prices:", negative_price_count)
    print("Zero quantities:", zero_quantity_count)

    # Final validation
    if (duplicate_count == 0
            and negative_price_count == 0
            and zero_quantity_count == 0):
        print("\nValidation passed")
    else:
        print("\nValidation failed")


if __name__ == "__main__":
    main()