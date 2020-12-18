"""
local modules
"""
# secrets
from secrets import psql_dsn
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
import os
import requests
import pyodbc

sb = string_builder()
qb = query_builder()
dr = data_reader()
qe = query_executor(pyodbc.connect(f"DSN={psql_dsn}"))

for filename in os.listdir('data_pipeline/data'):
    # file is opened
    key = filename[8]
    with open(f'data_pipeline/data/{filename}', 'r') as file_in:
        data = json.load(file_in)
        
        # skyfall is reassigned
        try: 
            data["current"]["rain_mm"] = data["current"]["rain"]["1h"]
            del data["current"]["rain"]
        except:
            data["current"]["rain_mm"] = 0
        try: 
            data["current"]["snow_mm"] = data["current"]["snow"]["1h"]
            del data["current"]
        except:
            data["current"]["snow_mm"] = 0

        # Conditions are reassigned as key-values
        data["current"]["condition_name"] = data["current"]["weather"][0]["main"]
        data["current"]["condition_description"] = data["current"]["weather"][0]["description"]
        
        del data["current"]["weather"]

        # The same transformation is applied to each forecast
        for item in data["hourly"]:
            # skyfall is reassigned
            try: 
                item["rain_mm"] = item["rain"]["1h"]
                del item["rain"]
            except:
                item["rain_mm"] = 0
            try: 
                item["snow_mm"] = item["snow"]["1h"]
                del item["snow"]
            except:
                item["snow_mm"] = 0

            item["condition_name"] = item["weather"][0]["main"]
            item["condition_description"] = item["weather"][0]["description"]
            
            del item["weather"]
            
        data_current_hourly = data["current"]
        del data_current_hourly["sunrise"]
        del data_current_hourly["sunset"]

        data_forecast_hourly = data["hourly"]

        df_current = pd.DataFrame(data_current_hourly, index=[0])
        df_current['pop'] = 0
        df_current["current_or_forecast"] = "Current"

        df_forecast = pd.DataFrame( data_forecast_hourly, index=range(1, len(data_forecast_hourly)+1) )
        df_forecast["current_or_forecast"] = "Forecast"

        df_combined = pd.concat([df_current, df_forecast])
        df_combined["location_key"] = key
        df_combined["dt"] = pd.to_datetime(df_combined['dt'], unit='s')
        df_combined["dt"] = df_combined["dt"].map(lambda dt: str(dt))
        
        # connection to PostgreSQL is created and rows are inserted
        print("Writing data.")
        column_string = """("datetime",Temperature,Feels_Like,Pressure,Humidity,Dew_Point,UVI,Clouds,
                            Visibility,Wind_Speed,Wind_Direction,Rain_mm,
                            Snow_mm,Condition_Name,Condition_Description,Probability_of_Precipitation,Current_or_Forecast,Location_Key)"""
        sql = qb.create_insert_statement('Weather_Hourly', column_string, sb.table_to_string(df_combined))
        qe.execute_query(f"DELETE FROM weather_hourly WHERE location_key = {key};")
        qe.execute_query(sql)
    # END with
# END for

qe.close_()

