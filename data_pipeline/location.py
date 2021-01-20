import requests
import pyodbc
import json

from secrets import geocodio_api_key, example_address

# variable assignment
base_uri = "https://api.geocod.io/v1.6/geocode"
params = {
    'api_key': geocodio_api_key,
    'q': example_address,
    'fields': 'timezone'
}
headers={'Accept': 'application/json'}

# request and response
response = requests.get(base_uri, params=params, headers=headers)
print(response.json())

