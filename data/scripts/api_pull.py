import requests 
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

# Chicago crime data API - limit to 5000 results for now
url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit=5000"

# Send the GET request
response = requests.get(url)

# Check response status
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Save to CSV
    output_path = "data/raw/chicago_crime_data.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved to {output_path}")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")

