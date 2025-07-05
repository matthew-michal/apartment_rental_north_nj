import requests
import json
import pandas as pd
import pickle

url = "https://api.rentcast.io/v1/listings/rental/long-term?state=NJ&status=Active&limit=50000"

headers = {
    "accept": "application/json",
    "X-Api-Key": "8856cfe498b1487bbebd1d0fd8ed545f"
}

response = requests.get(url, headers=headers)

print(response.text)

with open('data.bin','wb') as f_out:
    pickle.dump(response, f_out)

filtered_data = [{k: v for k, v in item.items() if k != "history"} for item in json.loads(response.text)]

# df = pd.DataFrame([filtered_data])
df = pd.DataFrame(filtered_data)
df.to_csv('second_load.csv', index=False)