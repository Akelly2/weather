"""
local modules
"""
# secrets
from secrets import psql_dsn, openweathermap_api_key
# local classes
from database_connector import query_executor, query_builder
from data_reader import data_reader
from string_builder import string_builder
"""
modules
"""
import pandas as pd
pd.set_option('max_colwidth', None)
import json
import requests
import pyodbc
import sys

sb = string_builder()
qb = query_builder()
dr = data_reader()

qe = query_executor(pyodbc.connect(f"DSN={psql_dsn}"))
sql = """ SELECT Location_Key, Latitude, Longitude FROM "Location" """
location_list = qe.get_results(sql, result_format="dict-list")

for location in location_list: 
    print('Accessing data for:', location["location_key"], location["latitude"], location["longitude"])

    # request and response is done
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/onecall',
        params={
            'lat': location["latitude"], 'lon': location["longitude"],
            'exclude': 'minutely,alerts',
            'units': 'metric',
            'appid': openweathermap_api_key
        },
        headers={'Accept': 'application/json'}
    )

    with open(f'data_pipeline/data/location{location["location_key"]}.json', 'w') as file_out:
        json.dump(response.json(), file_out)

