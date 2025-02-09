import pandas as pd
import os
from datetime import datetime, timedelta

# Initialize an empty DataFrame to store cumulative data
cumulative_data = pd.DataFrame()

df = pd.read_csv('okx_fundingrate_unzip/allswaprate-swaprate-2024-03-04.csv', encoding='utf-8')

# Correct column names from your CSV file
df.drop(['contract_type', 'funding_rate', 'funding_time'], axis=1,
        inplace=True)

# Group by 'instrument_name/交易币对名' and sum the 'real_funding_rate/本周期真实费率'
daily_rates = df.groupby('instrument_name')['real_funding_rate'].sum().reset_index()

# If cumulative DataFrame is empty, initialize it
if cumulative_data.empty:
    cumulative_data = daily_rates
    cumulative_data['days_count'] = 1
else:
    # Merge with cumulative data, summing rates and incrementing days count
    cumulative_data = cumulative_data.merge(daily_rates, on='instrument_name', how='outer',
                                            suffixes=('', '_new'))
    cumulative_data['real_funding_rate'] = cumulative_data.fillna(0)[
                                                              'real_funding_rate'] + \
                                                          cumulative_data.fillna(0)[
                                                              'real_funding_rate_new']
    cumulative_data.drop(['real_funding_rate_new'], axis=1, inplace=True)
    cumulative_data['days_count'] = cumulative_data['days_count'].fillna(0).astype(int) + 1
if cumulative_data['days_count'].max() == 30:
    cumulative_data['average_30_days'] = cumulative_data['real_funding_rate'] / 30
if cumulative_data['days_count'].max() == 60:
    cumulative_data['average_60_days'] = cumulative_data['real_funding_rate'] / 60


# 获取当前时间并格式化为字符串
current_time_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# 定义保存CSV文件的文件名，文件名包含当前时间
output_file_name = f"cumulative_data_{current_time_str}.csv"

# 将cumulative_data DataFrame保存到以当前时间命名的CSV文件中
cumulative_data.to_csv(output_file_name, index=False, encoding='utf-8')

print(f"Data saved to {output_file_name}")