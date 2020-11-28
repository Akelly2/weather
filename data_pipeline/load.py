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
import json
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
qe = query_executor(pyodbc.connect(f"DSN={psql_dsn}"))

# hourly data is written
with open('data_pipeline/data/test.json', 'r') as file_in:
    data = json.load(file_in)
    print(data)
    try:
        # appropriate data is selected
        

        # connection to PostgreSQL is created and rows are inserted
        print("Writing data.")
        column_string = """("datetime",Current_or_Forecast,Location_Key,Temperature,Feels_Like,Pressure,Humidity,
                            Dew_Point,Clouds,Visibility,REAL,Wind_Direction,Condition_Name,Condition_Description)"""
        sql = qb.create_insert_statement('security_price_daily', column_string, sb.table_to_string(df))
        qe.execute_query(sql)
        qe.close_()
    except:
        print("There was a problem.")

