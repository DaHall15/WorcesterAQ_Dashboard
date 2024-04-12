# The following base code was taken based off the following website:
# https://medium.com/@mahyar.aboutalebi/real-time-air-quality-mapping-in-4-easy-steps-python-3e4b7a09e2d3

# Defining the Area of Interest
import requests
url = "https://api.purpleair.com/v1/sensors"

# Coordinates of Worcester Area
nwlng = -71.88621040103936
nwlat = 42.325335608467334
selng = -71.72691479594192
selat = 42.216515499221515

# Querying the fields of the locations of the sensors within the area
querystring = { "fields": "latitude,altitude,longitude", "location_type": "0", "nwlng": f"{nwlng}", "nwlat": f"{nwlat}", "selng": f"{selng}", "selat": f"{selat}" }

# Setting the header of the request
headers = { "X-API-Key": "8DF7161D-F2AE-11EE-B9F7-42010A80000D"}

# This uses the requests package to query the sensor request
response = requests.get(url, headers=headers, params=querystring)

# Printing the response
print(response.text)


###########################

# Importing the necessary packages
import json
import pandas as pd # installed outside using pip install pandas in command prompt

# Defining 'response_dict' the responses as text into json
response_dict = json.loads(response.text)
# Creating a panda's dataframe
df = pd.DataFrame(response_dict['data'], columns=response_dict['fields'])
# Saving the dataframe in a CSV
df.to_csv('sensors.csv', index=False)

# Printing the output of the dataframe
df
# There are four total air quality sensors in Worcester from PurpleAir!

##################################################

# Downloading the Real-time air quality reaadings from sensors

import requests
from io import StringIO

# URL to pull the data
url = f"https://api.purpleair.com/v1/sensors"

# Coordinates of Worcester Area
nwlng = -71.88621040103936
nwlat = 42.325335608467334
selng = -71.72691479594192
selat = 42.216515499221515

# Setting the header of the request
headers = { "X-API-Key": "8DF7161D-F2AE-11EE-B9F7-42010A80000D"}

# Setting the parameters to get
params = {
    "fields": "pm2.5_atm",
    "location_type": "0",
    "nwlng": f"{nwlng}",
    "nwlat": f"{nwlat}",
    "selng": f"{selng}",
    "selat": f"{selat}"
}

response = requests.get(url, headers=headers, params=params)

# Importing from JSON to dataframe
import json
import io
data =  json.load(io.BytesIO(response.content))
df = pd.DataFrame(data['data'], columns=data['fields'])
# Save the dataframe in a CSV
df.to_csv('data.csv', index=False)
df