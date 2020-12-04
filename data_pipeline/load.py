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
    # print(data)
    # try:
    if 1 == 1:
        # neccessary data is collected
        # columns are created from nested JSON 
        
        # skyfall is reassigned
        try: 
            data["current"]["rain_mm"] = data["current"]["rain"]["1h"]
            del data["current"]["rain"]
        except:
            data["current"]["rain_mm"] = 0
            print("No rain.")
        try: 
            data["current"]["snow_mm"] = data["current"]["snow"]["1h"]
        except:
            data["current"]["snow_mm"] = 0
            print("No snow.")

        data["current"]["condition_name"] = data["current"]["weather"][0]["main"]
        data["current"]["condition_description"] = data["current"]["weather"][0]["description"]
        
        del data["current"]["weather"]
        
        
        print(data["current"])

        for item in data["hourly"]:
            print(item)
            # skyfall is reassigned
            try: 
                item["rain_mm"] = item["rain"]["1h"]
                del item["rain"]
            except:
                item["rain_mm"] = 0
                print("No rain.")
            try: 
                item["snow_mm"] = item["snow"]["1h"]
            except:
                item["snow_mm"] = 0
                print("No snow.")

            item["condition_name"] = item["weather"][0]["main"]
            item["condition_description"] = item["weather"][0]["description"]
            
            del item["weather"]
            

        print(data)

        with open('data_pipeline/data/test2.json', 'w') as file_out:
            json.dump(data, file_out)

        # connection to PostgreSQL is created and rows are inserted
        # print("Writing data.")
        # column_string = """("datetime",Current_or_Forecast,Location_Key,Temperature,Feels_Like,Pressure,Humidity,
        #                     Dew_Point,Clouds,Visibility,REAL,Wind_Direction,Condition_Name,Condition_Description)"""
        # sql = qb.create_insert_statement('security_price_daily', column_string, sb.table_to_string(df))
        # qe.execute_query(sql)
        # qe.close_()
    # except:
        # print("There was a problem.")

