import json
import requests
import pandas as pd

class data_reader:
    def __init__(self):
        pass

    def read_api_json_data(self, url):
        headers = {'Content-Type': 'application/json'}
        return requests.get(url, headers=headers)    

    def read_json_to_df(self, filename):
        df = pd.read_json(filename, orient='split')
        return df
