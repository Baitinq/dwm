#!/bin/python

import requests
import os

delim="|"

# Check for an internet connection
url='http://www.google.com/'
timeout=5
try:
    _ = requests.get(url, timeout=timeout)
    internet = True
except requests.ConnectionError:
    internet = False

COORDINATES = open("/usr/share/geolocate/.location", 'r').read()
LOCATION = "lat=" + COORDINATES.replace(":","&lon=")

API_KEY = "756edce7e9d4c385ef9499a53492678c"
UNITS = "Metric"
UNIT_KEY = "C"
#UNIT_KEY = "F"
LANG = "en"
#LANG = "nl"
#LANG = "hu"
if internet == True:
    API="http://api.openweathermap.org/data/2.5/weather?{}&lang={}&appid={}&units={}".format(LOCATION.strip(), LANG,  API_KEY, UNITS)
    REQ = requests.get(API)
    #REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=50.84660&lon=4.35280&lang=en&appid=756edce7e9d4c385ef9499a53492678c&units=Metric")
    try:
    # HTTP CODE = OK
        if REQ.status_code == 200:
            CURRENT = REQ.json()["weather"][0]["description"].capitalize()
            TEMP = int(float(REQ.json()["main"]["temp"]))
            print(" {}, {} °{}".format(CURRENT, TEMP, UNIT_KEY))
            print(delim)
        else:
            print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
    except (ValueError, IOError):
            print("Error: Unable print the data")
else:
    print("")
