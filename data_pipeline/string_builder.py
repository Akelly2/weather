import pandas as pd 

class string_builder:
    def __init__(self):
        pass

    def create_tiingo_url_daily(self, dates, token, symbol):
        startDate = dates[0]
        endDate = dates[1] 
        return f"https://api.tiingo.com/tiingo/daily/{symbol}/prices?startDate={startDate}&endDate={endDate}&token={token}"

    def create_tiingo_url_realtime(self, date, token, ticker):
        return f"https://api.tiingo.com/iex/{ticker}/prices?startDate={date}&resampleFreq=5min&token={token}"

    def column_list_to_string(self, list_):
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
