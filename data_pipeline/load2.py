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
with open('data_pipeline/testdata/test2.json', 'r') as file_in:
    data = json.load(file_in)

    data_current_hourly = data["current"]
    del data_current_hourly["sunrise"]
    del data_current_hourly["sunset"]

    data_forecast_hourly = data["hourly"]

    df_current = pd.DataFrame(data_current_hourly, index=[0])
    df_current["current_or_forecast"] = "Current"

    df_forecast = pd.DataFrame( data_forecast_hourly, index=range(1, len(data_forecast_hourly)+1) )
    df_forecast["current_or_forecast"] = "Forecast"

    df_combined = pd.concat([df_current, df_forecast])

    # connection to PostgreSQL is created and rows are inserted
        
    print("Writing data.")
    column_string = """("datetime",Current_or_Forecast,Location_Key,Temperature,Feels_Like,Pressure,Humidity,
                        Dew_Point,Clouds,Visibility,REAL,Wind_Direction,Condition_Name,Condition_Description)"""
    sql = qb.create_insert_statement('Weather_Hourly', column_string, sb.table_to_string(df_combined))
    qe.execute_query(sql)
    qe.close_()

    print(df_combined.head())
