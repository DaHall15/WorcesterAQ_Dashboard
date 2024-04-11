# Worcester Air Quality Project

Danielle Hall
Spatial Databases

## Project Objectives
- Develop a web-based dashboard that displays live air quality (Particulate Matter 2.5) readings from all public air quality sensors in the town of Worcester.  

- Utilize all current air quality monitors and their live data readings.  

- Create a readable and easily accessible web-based dashboard, it is hoped that residents will have a better understanding of their local air quality.  

- APIs will be used to query live data from PurpleAir and AirNOW 

- A python script will be developed to read the data into tables 

- The mapping platform chosen for this will be mapbox.

## Background
- PurpleAir, AirNOW and MassDEP are the three providers of air quality sensors that provide live air quality readings to the public. 
- Particulate Matter 2.5 (PM2.5) are harmful particulates in the air, not visible to the naked eye. 
- With increasing surface air temperatures and the urban heat island effect, it is vital residents of Worcester have a user-friendly web-based dashboard to view live readings of air quality (measured by PM2.5) in their neighborhood.

## Proposed Workflow
<img width="600px" src="Images\initial_workflowproposal.png" alt="workflow"></img>


### PurpleAir Python File 


### AirNOW Python File 


### Example Code
- This is an example GitHub that seems to consolodate the live data feeds from AirNOW, and PurpleAir: https://github.com/bastienwirtz/aqi_watcher.git 

#### Querying AirNOW:
```
"""
Airnow data source
https://www.airnow.gov/
"""

import pytz
import requests
import settings
from datetime import datetime


def get_points(postcode):
    aqi_query = requests.get(
        f"https://airnowapi.org/aq/observation/zipCode/current?zipCode={postcode}&format=json&api_key={settings.AIRNOW_KEY}"
    )
    aqi_query.raise_for_status()
    aqi = aqi_query.json()

    points = []
    for entry in aqi:
        report_date = pytz.timezone("US/Pacific").localize(
            datetime.strptime(entry["DateObserved"].strip(), "%Y-%m-%d").replace(
                hour=entry["HourObserved"]
            )
        )
        report_date = int(report_date.astimezone(pytz.utc).timestamp()) * 1000000000

        points.append(
            {
                "measurement": entry["ParameterName"],
                "tags": {"location": entry["ReportingArea"], "postcode": postcode},
                "time": report_date,
                "fields": {
                    "aqi": entry["AQI"],
                    "zone": entry["Category"]["Number"],
                    "libelle": entry["Category"]["Name"],
                },
            }
        )

    return points
```

#### Querying PurpleAir:
```
"""
Purpleair data source
https://www2.purpleair.com/community/faq#!hc-access-the-json
"""

import requests


def get_points(sensor_id):
    purple_query = requests.get(f"https://www.purpleair.com/json?show={sensor_id}")
    purple_query.raise_for_status()
    purple = purple_query.json()

    points = []
    for sensor in purple["results"]:
        points.append(
            {
                "measurement": "purpleair",
                "tags": {"location": sensor["Label"], "sensor": sensor_id},
                "time": sensor["LastSeen"] * 1000000000,
                "fields": {
                    "pm2_5": float(sensor["pm2_5_atm"]),
                    "pm1_0": float(sensor["pm1_0_atm"]),
                    "pm10_0": float(sensor["pm10_0_atm"]),
                },
            }
        )
    return points
```