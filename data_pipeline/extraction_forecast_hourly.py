"""
local modules
"""
from database_connector import query_executor, query_builder
from data_reader import data_reader
from string_builder import string_builder
from secrets import openweathermap_api_key
"""
modules
"""
import pandas as pd
pd.set_option('max_colwidth', None)
import io
import requests
import pyodbc
import sys
from datetime import datetime, timedelta

sb = string_builder()
qb = query_builder()
dr = data_reader()

# qe = query_executor(pyodbc.connect(f"DSN={psql_dsn}"))
# request and response is done
response = requests.get(
    'https://api.openweathermap.org/data/2.5/onecall',
    params={'lat': 49.2827, 'lon': 123.1207, 'exclude': 'minutely', 'appid': openweathermap_api_key},
    headers={'Accept': 'application/json'}
)
print(response.json())

# df = pd.read_json(io.StringIO(response.content.decode('utf-8')))

