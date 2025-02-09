import pandas as pd

def update_csv_files():
    # Define new column names
    new_columns = [
        'instrument_name/交易币对名', 'contract_type/合约类型', 'funding_rate/预测下一周期费率', 'real_funding_rate/本周期真实费率', 'funding_time/下一周期时间戳'
    ]

    # Loop through all months from January (01) to December (12)
    for month in range(1, 13):
        for day in range(1, 32):
            # Format the file name based on the month
            file_name = f'okx_fundingrate_unzip/allswaprate-swaprate-2021-{month:02d}-{day:02d}.csv'

            try:
                # Read the CSV file assuming it has no header
                df = pd.read_csv(file_name, header=None)

                # Assign new column names to the dataframe
                df.columns = new_columns

                # Save the updated dataframe to the same CSV file
                df.to_csv(file_name, index=False, header=True, encoding='utf_8_sig')
                print(f"Updated file: {file_name}")
            except FileNotFoundError:
                print(f"File not found: {file_name}")
            except Exception as e:
                print(f"An error occurred with file: {file_name}, Error: {e}")


# Call the function to update the CSV files
update_csv_files()