# R SCript to read in RSS feed to python
# April 04 2024

#https://practicaldatascience.co.uk/data-science/how-to-read-an-rss-feed-in-python

# Importing the packages
import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

# Parse the RSS feed contents
## Since we already have the HTML provided from the AirNOW xml, we'll use that


