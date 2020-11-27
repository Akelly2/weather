import pandas as pd 

class string_builder:
    def __init__(self):
        pass

    def column_list_to_string(self, list_: list):
        list_ = tuple(list_)
        string_list = str(list_)
        return string_list

    def table_to_string(self, df: pd.DataFrame):
        table_string = ""
        table_string = df.apply(lambda row: str(tuple(row))+',', 1).to_string(index=False) 
        table_string = table_string.rstrip(',')
        return table_string 


# sb = string_builder()
# df = pd.DataFrame({'col1': [1,2], 'col2': [3, 4]})
# print( sb.list_to_string(df.columns) )
# print( sb.table_to_string(df) )
# print(sb.table_to_string(df))
