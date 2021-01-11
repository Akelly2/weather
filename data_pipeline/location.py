import requests
import pyodbc

import json
import time
import urllib.error
import urllib.parse
import urllib.request

from secrets import google_maps_api_key
print(google_maps_api_key)

uri = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=49,-123&radius=500&types=food&name=harbour&key={google_maps_api_key}"

geocoding_base_uri = "https://maps.googleapis.com/maps/api/geocode/json"


City = "Vancouver"
Region = "BC"
Country = "CA"
params = urllib.parse.urlencode(
        {"address": f"{City},{Region},{Country}", "key": google_maps_api_key}
    )
url = f"{geocoding_base_uri}?{params}"
response = urllib.request.urlopen(url)
result = json.load(response)
print(result)

# timezone_base_uri = ""
