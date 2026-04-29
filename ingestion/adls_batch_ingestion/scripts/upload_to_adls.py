def process_all_files():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv") or file.endswith(".csv.gz"):

            file_path = os.path.join(DATA_DIR, file)

            parquet_path, parquet_name = convert_to_parquet(file_path)
            upload_to_adls(parquet_path, parquet_name)

    print("\nAll files processed successfully!")
