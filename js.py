import requests
import os


def get_file_list_for_month(month):
    """Get the list of files for a given month."""
    api_url = f'https://www.okx.com/priapi/v5/broker/public/v2/orderRecord'
    params = {
        'path': f'cdn/okex/traderecords/swaprate/monthly/{month}',
        'nextMarker': '',
        'size': '30',  # Adjust if needed
        't': '1709720472250'  # Adjust if needed
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('recordFileList', [])
    else:
        print(f'Error fetching file list for month {month}: {response.status_code}')
        return []


# List of months you want to download files for
months = [
    "202403", "202402", "202401", "202312", "202311", "202310",
    "202309", "202308", "202307", "202306", "202305", "202304",
    "202303", "202302", "202301", "202212", "202211", "202210",
    "202209", "202208", "202207", "202206", "202205", "202204",
    "202203", "202202", "202201", "202112", "202111", "202110"
]

# Download directory
download_dir = 'okx_fundingrate'
os.makedirs(download_dir, exist_ok=True)  # Ensure the directory exists

# Loop through the list of months and download the files for each
for month in months:
    file_list = get_file_list_for_month(month)
    for file_info in file_list:
        file_name = file_info['fileName']
        download_url = f'https://www.okx.com/cdn/okex/traderecords/swaprate/monthly/{month}/{file_name}'
        print(f'Downloading {file_name} from {month}...')

        # Send a GET request to download the file
        file_response = requests.get(download_url)

        # Check if the download was successful
        if file_response.status_code == 200:
            # Save the file to the download directory
            file_path = os.path.join(download_dir, f"{file_name}")
            with open(file_path, 'wb') as file:
                file.write(file_response.content)
            print(f'Download complete: {file_path}')
        else:
            print(f'Error downloading {file_name} from {month}: {file_response.status_code}')