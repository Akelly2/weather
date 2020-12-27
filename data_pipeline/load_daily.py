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
    key = int(filename[8])
    with open(f'data_pipeline/data/{filename}', 'r') as file_in:
        json_data = json.load(file_in)

        # The same transformation is applied to each forecast
        for item in json_data["daily"]:
            # skyfall is reassigned
            try: 
                item["rain_mm"] = item["rain"]
                del item["rain"]
            except:
                item["rain_mm"] = 0
            try: 
                item["snow_mm"] = item["snow"]
                del item["snow"]
            except:
                item["snow_mm"] = 0

            # each temp is pulled out
            for thing in ["day", "min", "max", "night", "eve", "morn"]:
                item[thing + "_temp"] = item["temp"][thing]

            # each feels_like temp is pulled out
            for thing in ["day", "night", "eve", "morn"]:
                item[thing + "_fl"] = item["feels_like"][thing]

            item["condition_name"] = item["weather"][0]["main"]
            item["condition_description"] = item["weather"][0]["description"]
            item["icon"] = item["weather"][0]["icon"]
            
            del item["weather"]
            del item["temp"]
            del item["feels_like"]

        data_forecast_daily = json_data["daily"]

        df_forecast = pd.DataFrame( data_forecast_daily, index=range(1, len(data_forecast_daily)+1) )
        df_forecast["location_key"] = key
        df_forecast["current_or_forecast"] = "Forecast"

        df_forecast["dt"] = pd.to_datetime(df_forecast['dt'], unit='s')
        df_forecast["sunrise"] = pd.to_datetime(df_forecast['sunrise'], unit='s')
        df_forecast["sunset"] = pd.to_datetime(df_forecast['sunset'], unit='s')
        
        df_forecast["dt"] = df_forecast["dt"].map(lambda dt: str(dt))
        df_forecast["sunrise"] = df_forecast["sunrise"].map(lambda dt: str(dt))
        df_forecast["sunset"] = df_forecast["sunset"].map(lambda dt: str(dt))

        # connection to PostgreSQL is created and rows are inserted
        print("Writing data.")
        column_string = """
            ("datetime",Sunrise,Sunset,Pressure,Humidity,Dew_Point,Wind_Speed,Wind_Direction,
            Clouds,Probability_of_Precipitation,UVI,Rain_mm,Snow_mm,
            Day_Temp,Min_Temp,Max_Temp,Night_Temp,Evening_Temp,
            Morning_Temp,Day_FL,Night_FL,Evening_FL,Morning_FL,Condition_Name,
            Condition_Description,Icon_Code,Location_Key,Current_or_Forecast) """
        sql = qb.create_insert_statement('Weather_Daily', column_string, sb.table_to_string(df_forecast))
        qe.execute_query(f"DELETE FROM weather_daily WHERE location_key = {key};")
        qe.execute_query(sql)
    # END with
# END for

qe.close_()

