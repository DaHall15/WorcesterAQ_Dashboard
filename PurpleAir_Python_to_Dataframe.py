# The following base code was taken based off the following website:
# https://medium.com/@mahyar.aboutalebi/real-time-air-quality-mapping-in-4-easy-steps-python-3e4b7a09e2d3

# Defining the Area of Interest
import requests
url = "https://api.purpleair.com/v1/sensors" # This is the basic url, it will be added to
# Coordinates of Worcester Area - area of interest
nwlng = -71.88621040103936
nwlat = 42.325335608467334
selng = -71.72691479594192
selat = 42.216515499221515

# Querying the fields of the locations of the sensors within the area
querystring = {"fields": "latitude,altitude,longitude",
               "location_type": "0","nwlng": f"{nwlng}", "nwlat": f"{nwlat}", "selng": f"{selng}", "selat": f"{selat}"}

# Setting the header of the request, this is the read API key
headers = { "X-API-Key": "8DF7161D-F2AE-11EE-B9F7-42010A80000D"}
# This uses the requests package to query the sensor requests, combining the url, header and parameters into a single request/query
response = requests.get(url, headers=headers, params=querystring)
# Printing the response to the query
print(response.text)

########################### CREATING A DB FOR SENSORS ##########################

# Importing the necessary packages
import json
import pandas as pd

# Defining 'response_dict' the responses as text into json
response_dict = json.loads(response.text)
response_dict['time_stamp']
# Creating a panda's dataframe
df_sensors = pd.DataFrame(response_dict['data'], columns=response_dict['fields']) # creates dataframe with all listed fields
# Adding time stamp to the data frame
response_dict['data']
df_sensors['time_stamp'] = response_dict['time_stamp']
# Printing the output of the dataframe
df_sensors # There are four total air quality sensors in Worcester from PurpleAir!
# Then add convert to csv...?
df_sensors.to_csv('sensors.csv', index=False)

####################### CREATING A DB FOR Air Quality Readings ##########################
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

# Setting the header of the request - again we have the READ API key
headers = { "X-API-Key": "8DF7161D-F2AE-11EE-B9F7-42010A80000D"}
#
# Setting the parameters to get
params = {
    "fields": "pm2.5_60minute", # The parameters queried are PM2.5 for 60 minute
    "location_type": "0",# changed to fields_aq to distinguish between params
    "nwlng": f"{nwlng}",
    "nwlat": f"{nwlat}",
    "selng": f"{selng}",
    "selat": f"{selat}"
}


response = requests.get(url, headers=headers, params=params) # combines the parts into one query
# Importing from JSON to dataframe
import json
import io

data =  json.load(io.BytesIO(response.content)) 
df_aq = pd.DataFrame(data['data'], columns=data['fields']) # puts the response into a dataframe
# Printing the dataframe
df_aq

# Normalization Steps
# - Add timestamp
# - Add sensor name

# Save the dataframe in a CSV                ### EXPORTING DATAFRAME OF ACTUAL AIRQUALITY READINGS ###
df_aq.to_csv('data.csv', index=False)

################################# Joining the Dataframes ###########################################
import json
import io
data =  json.load(io.BytesIO(response.content))
df_all = pd.DataFrame(data['data'], columns=data['fields'])

import pandas as pd
df1 = pd.read_csv('sensors.csv')
df2 = pd.read_csv('data.csv')

merged_df = pd.merge(df1, df2, on='sensor_index')
merged_df.to_csv('sensors_data.csv', index=False)
merged_df


###################### Normalizing the Data Frame ###############################33

# Dropping Unnecessary columns
merged_df_norm = merged_df.drop('altitude', axis =1)
merged_df_norm

# Add sensor name based on PurpleAir Sensor info
sensor_id_purpleair = ['Mass. DEP PurpleAir', 'Forest Grove', 'Batters Eye Polar Park', 'Batters Eye 2']
merged_df_norm.loc[:,"SensorName"]= sensor_id_purpleair
merged_df_norm

# Changing the order of the columns
merged_df_norm.iloc[:,[5,4,3,1,2,0]] ## Then need to save this permanentely 
