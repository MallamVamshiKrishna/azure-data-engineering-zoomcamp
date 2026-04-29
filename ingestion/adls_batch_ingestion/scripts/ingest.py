import os
import pandas as pd
from azure.storage.blob import BlobServiceClient

# ==============================
# 🔐 CONFIGURATION
# ==============================

# Folder where your CSV files exist
DATA_DIR = "../data"   # (since script is inside scripts/ folder)

# Azure Storage connection (use environment variable)
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Container name in ADLS
CONTAINER_NAME = "nyc-taxi-data"


# ==============================
# ☁️ CONNECT TO ADLS
# ==============================

blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)


# ==============================
# 📦 CONVERT CSV → PARQUET
# ==============================

def convert_to_parquet(file_path):
    print(f"Reading: {file_path}")

    # Pandas can read .csv and .csv.gz
    df = pd.read_csv(file_path)

    # Optional: convert datetime columns if present
    if 'tpep_pickup_datetime' in df.columns:
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    if 'tpep_dropoff_datetime' in df.columns:
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Create parquet file name
    parquet_file = os.path.basename(file_path) \
        .replace(".csv.gz", ".parquet") \
        .replace(".csv", ".parquet")

    parquet_path = os.path.join(DATA_DIR, parquet_file)

    # Save parquet
    df.to_parquet(parquet_path, engine="pyarrow", index=False)

    print(f"Converted → {parquet_file}")

    return parquet_path, parquet_file


# ==============================
# 📤 UPLOAD TO ADLS
# ==============================

def upload_to_adls(parquet_path, blob_name):
    blob_client = container_client.get_blob_client(blob_name)

    # Skip if file already exists
    if blob_client.exists():
        print(f"Skipping (already exists): {blob_name}")
        return

    with open(parquet_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"Uploaded → {blob_name}")


# ==============================
# 🔁 PROCESS ALL FILES
# ==============================

def process_all_files():
    print("Starting ingestion...\n")

    for file in os.listdir(DATA_DIR):

        if file.endswith(".csv") or file.endswith(".csv.gz"):

            file_path = os.path.join(DATA_DIR, file)

            print(f"\nProcessing: {file}")

            parquet_path, parquet_name = convert_to_parquet(file_path)

            upload_to_adls(parquet_path, parquet_name)

    print("\nAll files processed successfully!")


# ==============================
# 🚀 MAIN
# ==============================

if __name__ == "__main__":
    process_all_files()

