import numpy as np
import pandas as pd
import json
from string_builder import string_builder

import pyodbc
from imports import dsn

sb = string_builder()

class file_writer:
    def __init__(self):
        pass

    def write_json_file(self, filename, response):   
        with open(f"{filename}.json", 'w') as f:
            json.dump({'data': response.json()}, f, ensure_ascii=False)

