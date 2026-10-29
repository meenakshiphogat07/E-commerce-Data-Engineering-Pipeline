"""Investigate cancellations, returns, missing customers, and revenue."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"


def main() -> None:
    """Load the retail dataset and display the existing investigation samples."""
    data = pd.read_excel(INPUT_FILE)

    negative_quantity = data.loc[
        data["Quantity"] < 0,
        ["InvoiceNo", "StockCode", "Quantity", "UnitPrice", "Country"],
    ]
    cancelled_invoices = data.loc[
        data["InvoiceNo"].str.startswith("C", na=False)
    ]
    missing_customers = data.loc[data["CustomerID"].isna()]
    data["Revenue"] = data["Quantity"] * data["UnitPrice"]

    print(negative_quantity.head(10))
    print(cancelled_invoices.head(10))
    print(missing_customers.head(10))
    print(data[["InvoiceNo", "Quantity", "UnitPrice", "Revenue"]].head())


if __name__ == "__main__":
    main()
