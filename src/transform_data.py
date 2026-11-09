
from pathlib import Path
from ingest_data import ingest_data
from clean_data import clean_data


def main() -> None:
    """Load, clean, transform, and save the retail dataset."""

    # Step 1: Ingest raw data
    data = ingest_data()

    # Step 2: Clean data
    cleaned_data = clean_data(data)

    # Step 3: Calculate revenue
    cleaned_data["Revenue"] = (
        cleaned_data["Quantity"] * cleaned_data["UnitPrice"]
    )

    
    cleaned_data["InvoiceNo"] = cleaned_data["InvoiceNo"].astype("string")

    cleaned_data["StockCode"] = cleaned_data["StockCode"].astype("string")

    cleaned_data["Description"] = cleaned_data["Description"].astype("string")

    # Step 4: Display data quality and transformation details
    print(f"Rows before cleaning: {len(data)}")
    print(f"Columns before cleaning: {len(data.columns)}")
    print(f"Rows after cleaning: {len(cleaned_data)}")
    print(f"Columns after cleaning: {len(cleaned_data.columns)}")
    print(f"Rows removed: {len(data) - len(cleaned_data)}")

    print("\nFirst 5 transformed records:")
    print(cleaned_data[["Quantity", "UnitPrice", "Revenue"]].head())

    print(f"\nTotal revenue: {cleaned_data['Revenue'].sum():.2f}")

    print("\nData types before saving:")
    print(cleaned_data.dtypes)


    # Step 5: Create output directory
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 6: Save as Parquet
    output_file = output_dir / "retail_cleaned.parquet"
    cleaned_data.to_parquet(output_file, index=False)

    print(f"\nParquet file saved successfully: {output_file}")


if __name__ == "__main__":
    main()
  