import pandas as pd

def update_csv_files():
    # Define new column names without Chinese
    new_columns = [
        'instrument_name', 'contract_type', 'funding_rate', 'real_funding_rate', 'funding_time'
    ]

    # Loop through all months from January (01) to December (12)
    for month in range(1, 13):
        for day in range(1, 32):
            # Format the file name based on the month and day
            file_name = f'okx_fundingrate_unzip/allswaprate-swaprate-2024-{month:02d}-{day:02d}.csv'

            try:
                # Read the CSV file with the specified encoding
                df = pd.read_csv(file_name, encoding='gbk')  # Specify the encoding here

                # Check if the dataframe has the expected number of columns to avoid errors when assigning new column names
                if df.shape[1] == len(new_columns):
                    # Replace the original column names with new column names
                    df.columns = new_columns

                    # Save the updated dataframe to the same CSV file
                    df.to_csv(file_name, index=False, header=True, encoding='utf-8')  # Write the file with the same encoding
                    print(f"Updated file: {file_name}")
                else:
                    print(f"Column count mismatch in file: {file_name}")
            except FileNotFoundError:
                print(f"File not found: {file_name}")
            except Exception as e:
                print(f"An error occurred with file: {file_name}, Error: {e}")

# Call the function to update the CSV files
update_csv_files()