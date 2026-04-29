def process_all_files():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv") or file.endswith(".csv.gz"):

            file_path = os.path.join(DATA_DIR, file)

            parquet_path, parquet_name = convert_to_parquet(file_path)
            upload_to_adls(parquet_path, parquet_name)

    print("\nAll files processed successfully!")


# from azure.storage.blob import BlobServiceClient
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
