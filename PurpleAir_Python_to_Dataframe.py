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
