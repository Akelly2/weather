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
        
        # skyfall is reassigned
        try: 
            json_data["current"]["rain_mm"] = json_data["current"]["rain"]["1h"]
            del json_data["current"]["rain"]
        except:
            json_data["current"]["rain_mm"] = 0
        try: 
            json_data["current"]["snow_mm"] = json_data["current"]["snow"]["1h"]
            del json_data["current"]
        except:
            json_data["current"]["snow_mm"] = 0

        # Conditions are reassigned as key-values
        json_data["current"]["condition_name"] = json_data["current"]["weather"][0]["main"]
        json_data["current"]["condition_description"] = json_data["current"]["weather"][0]["description"]
        
        del json_data["current"]["weather"]

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
            
            del item["weather"]
            del item["temp"]
            del item["feels_like"]
            
        data_current_daily = json_data["current"]
        del data_current_daily["sunrise"]
        del data_current_daily["sunset"]

        data_forecast_daily = json_data["daily"]

        df_current = pd.DataFrame(data_current_daily, index=[0])
        df_current['pop'] = 0
        df_current["current_or_forecast"] = "Current"

        df_forecast = pd.DataFrame( data_forecast_daily, index=range(1, len(data_forecast_daily)+1) )
        df_forecast["current_or_forecast"] = "Forecast"

        df_combined = pd.concat([
            df_current, 
            df_forecast])
        df_combined["location_key"] = key

        df_combined["dt"] = pd.to_datetime(df_combined['dt'], unit='s')
        df_combined["sunrise"] = pd.to_datetime(df_combined['sunrise'], unit='s')
        df_combined["sunset"] = pd.to_datetime(df_combined['sunset'], unit='s')
        
        df_combined["dt"] = df_combined["dt"].map(lambda dt: str(dt))
        df_combined["sunrise"] = df_combined["sunrise"].map(lambda dt: str(dt))
        df_combined["sunset"] = df_combined["sunset"].map(lambda dt: str(dt))
        
        print(df_combined.columns)

        # connection to PostgreSQL is created and rows are inserted
        print("Writing data.")
        column_string = """
            ("datetime",Temperature,Feels_Like,Pressure,Humidity,
            Dew_Point,UVI,Clouds,Visibility,Wind_Speed,Wind_Direction,Rain_mm,Snow_mm,Condition_Name,
            Condition_Description,Probability_of_Precipitation,Current_or_Forecast,Sunrise,Sunset,
            Day_Temp,Min_Temp,Max_Temp,Night_Temp,Evening_Temp,
            Morning_Temp,Day_FL,Night_FL,Evening_FL,Morning_FL,Location_Key) """
        sql = qb.create_insert_statement('Weather_Daily', column_string, sb.table_to_string(df_combined))
        print(sql)
        qe.execute_query(f"DELETE FROM weather_daily WHERE location_key = {key};")
        qe.execute_query(sql)
    # END with
# END for

qe.close_()

