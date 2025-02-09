import pandas as pd


def detect_encoding(file_name):
    # List of encodings to try
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030']

    for encoding in encodings:
        try:
            # Attempt to read the file with the specified encoding
            df = pd.read_csv(file_name, encoding=encoding)
            # If the file is read without raising an exception, the encoding is likely correct
            print(f"Successfully read {file_name} with encoding: {encoding}")
            return encoding  # Return the successful encoding
        except UnicodeDecodeError:
            # If a UnicodeDecodeError is raised, try the next encoding
            continue
        except Exception as e:
            # Catch any other exceptions and print the error message
            print(f"An error occurred: {e}")
            break  # Exit the loop if an unexpected error occurs

    return None  # Return None if no encodings were successful


# Replace 'your_file_path.csv' with the path to your CSV file
encoding_detected = detect_encoding('okx_fundingrate_unzip/allswaprate-swaprate-2022-01-01.csv')
if encoding_detected:
    print(f"The likely encoding for the file is: {encoding_detected}")
else:
    print("Failed to detect encoding.")