import boto3

s3_client = boto3.client(
    "s3",
    region_name="eu-north-1"
)

print("S3 client created successfully.")

def upload_file_to_s3(file_path: str, bucket_name: str, s3_key: str) -> None:
    """Upload a file to an S3 bucket."""
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded to {bucket_name}/{s3_key} successfully.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        raise

upload_file_to_s3(
    "data/raw/Online Retail.xlsx",
    "ecommerce-data-pipeline-meenakshi",
    "raw/Online Retail.xlsx"
)

upload_file_to_s3(
    "data/processed/retail_cleaned.parquet",
    "ecommerce-data-pipeline-meenakshi",
    "processed/retail_cleaned.parquet"
)

print("File upload process completed.")

def list_s3_files(bucket_name: str) -> None:
    """List files in the specified S3 bucket."""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"File: {obj['Key']}, Size: {obj['Size']} bytes")
        else:
            print("No files found in the bucket.")
    except Exception as e:
        print(f"Error listing files in S3 bucket: {e}")
        raise

list_s3_files("ecommerce-data-pipeline-meenakshi")

