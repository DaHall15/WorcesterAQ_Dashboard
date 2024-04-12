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
### Purple Air Interactive Map
<img width="600px" src="Images\purpleair_interactivemap.png" alt="workflow"></img>

### AirNOW Interactive Map 
<img width="600px" src="Images\airnow_interactivemap.png" alt="workflow"></img>
## Proposed Workflow
Follow the proposed workflow in the diagram below. 
<img width="600px" src="Images\workflow_part1.png" alt="workflow"></img>

<img width="600px" src="Images\workflow_part2.png" alt="workflow"></img>

## PurpleAir Script to Read in Data Feed - Step 3
Purple Air live data feed will be read into a dataframe (and eventually a csv) using the example code provided in a 'Medium' article: https://medium.com/@mahyar.aboutalebi/real-time-air-quality-mapping-in-4-easy-steps-python-3e4b7a09e2d3 

The example code was used and adapted for this project in the file named _"PurpleAir_Python_to_Dataframe.py"_ witihn this repo. 

## AirNOW Script to Read in Data Feed - Step 3
AirNOW data live data feed will be read into a dataframe and csv, using the example code from Practical Data Science page: https://practicaldatascience.co.uk/data-science/how-to-read-an-rss-feed-in-python 

Example code was adapted to the use of this project and is called _"AirNOW_RSS_feedtoPython.py"_ in this repo.

## Required packages
Make sure to download the packages required to run this code. Use the "required_packages" text file within this repo for required packages

## CalEnviroScreen Example
The final dashboard devleoped is aimed to emulate the basic structure of the CalEnviroScreen dashboard hosted on ArcGIS online. See the website here: https://experience.arcgis.com/experience/11d2f52282a54ceebcac7428e6184203/page/CalEnviroScreen-4_0/ 