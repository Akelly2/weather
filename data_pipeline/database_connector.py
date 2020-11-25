import numpy as np
import pandas as pd
import json

import pyodbc

class query_builder:
    def __init__(self):
        pass

    def create_insert_statement(self, table_name: str, column_names: str, column_values: str):
        sql = f"""
            INSERT INTO 
                {table_name} {column_names}
            VALUES
                {column_values}
        """
        return sql
    
    def create_upsert_statement(self):
        pass

    def create_update_statement(self):
        pass


class query_executor:
    def __init__(self, connector: pyodbc.Connection):
        self.connector = connector
        
    def get_results(self, sql):
        # try: 
            return pd.read_sql(sql, self.connector)
        # except:
            # return 'There was a problem.' 

    def execute_query(self, sql):
        try: 
            cursor = self.connector.cursor()
            cursor.execute(sql)
            cursor.commit()
            cursor.close()
            return "Query execution success."
        except: 
            cursor.close()
            return "Query execution failed."    
            
    def close_(self):
        self.connector.close()
