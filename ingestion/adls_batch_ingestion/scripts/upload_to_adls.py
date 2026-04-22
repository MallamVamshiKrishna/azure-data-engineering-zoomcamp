import os
from azure.storage.blob import BlobServiceClient


# -------------------------------
# CONFIGURATION
# -------------------------------
ACCOUNT_NAME = "vamshiadls123"
ACCOUNT_KEY ="YOUR_ACCESS_KEY"
CONTAINER_NAME = "nyc-taxi-data"
FILE_NAME = "yellow_tripdata.parquet"


# -------------------------------
# FUNCTION: Get File Path
# -------------------------------
def get_file_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(current_dir)

    file_path = os.path.join(base_dir, "data", file_name)

    print(f"[INFO] File path resolved: {file_path}")
    return file_path


# -------------------------------
# FUNCTION: Connect to Azure
# -------------------------------
def get_container_client():
    connection_string = (
        f"DefaultEndpointsProtocol=https;"
        f"AccountName={ACCOUNT_NAME};"
        f"AccountKey={ACCOUNT_KEY};"
        f"EndpointSuffix=core.windows.net"
    )

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    print("[INFO] Connected to Azure Storage")
    return container_client


# -------------------------------
# FUNCTION: Upload File
# -------------------------------
def upload_file(container_client, file_path, blob_name):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] File not found: {file_path}")

    print(f"[INFO] Uploading file: {blob_name}")

    with open(file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)

    print("[SUCCESS] File uploaded successfully!")


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    file_path = get_file_path(FILE_NAME)
    container_client = get_container_client()
    upload_file(container_client, file_path, FILE_NAME)


# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    main()


# from azure.storage.blob import BlobServiceClient
#dataengineerin interview for me for tommorow

# account_name = "vamshiadls123"
# account_key = "YOUR_ACCESS_KEY"
# container_name = "nyc-taxi-data"


# connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# container_client = blob_service_client.get_container_client(container_name)

# file_path = "data/yellow_tripdata.parquet"
# blob_name = "yellow_tripdata.parquet"

# with open(file_path, "rb") as data:
#     container_client.upload_blob(name=blob_name, data=data, overwrite=True)
