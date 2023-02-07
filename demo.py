import requests
import pandas as pd
import json
from datetime import datetime
# using time module
#import time

# ts stores the time in seconds
#ts = time.time()

# import module
from datetime import datetime
  
# get current date and time
current_datetime = datetime.now()
payload={}
headers = {
  'Authorization': 'Bearer d47433f8-9a33-47c7-ba43-1a0fbac28f55'
}
# Date = datetime.now().strftime('%Y-%m-%d')

Date = '2022-09-15'
url = f"https://dev-retail-api.tangoeye.ai/v1/processedDayData?limit=3000&fromDate={Date}&toDate={Date}"
response = requests.request("GET", url, headers=headers, data=payload)
response_json = json.loads(response.text)
total_count = response_json['data']['count']
print("count: ", total_count)
df = pd.DataFrame(response_json['data']['data'])
df.to_csv(f'/home/rajesh/Airflow_output/out_dailydata{current_datetime}'+'.csv')
