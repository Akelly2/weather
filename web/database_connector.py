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
        
    def get_results(self, sql, params=(), result_format="df"):
        if result_format == "df":
            return pd.read_sql(sql, self.connector)
        elif result_format == "dict-list":
            cursor = self.connector.cursor()
            cursor.execute(sql, params)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            cursor.close()
            return results

    def execute_query(self, sql):
        cursor = self.connector.cursor()
        cursor.execute(sql)
        cursor.commit()
        cursor.close()    
            
    def close_(self):
        self.connector.close()
