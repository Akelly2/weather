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
    with open(f'data_pipeline/data/{filename}', 'r') as file_in:
        # data is read
        json_data = json.load(file_in)

        try: 
            data_alerts = json_data["alerts"]
            print(data_alerts)

            df_alerts = pd.DataFrame( data_alerts, index=range(1, len(data_alerts)+1) )
            
            # unix timetamps are converted to dates
            df_alerts["start"] = pd.to_datetime(df_alerts['start'], unit='s')
            df_alerts["end"] = pd.to_datetime(df_alerts['end'], unit='s')

            # dates are converted to strings
            df_alerts["start"] = df_alerts["start"].map(lambda dt: str(dt))
            df_alerts["end"] = df_alerts["end"].map(lambda dt: str(dt))

            df_alerts["location_key"] = key

            print("Writing data.")
            column_string = """
                (Sender, Event_Name, Start_Time, End_Time, Event_Description, Location_Key) """
            sql = qb.create_insert_statement('Alert', column_string, sb.table_to_string(df_alerts))
            qe.execute_query(f"DELETE FROM Alert WHERE location_key = {key};")
            qe.execute_query(sql)
        except:
            "No alerts were written."


