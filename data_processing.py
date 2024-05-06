import pandas as pd

def read_csv_files(file_path) :
    df = pd.read_csv(file_path)
    return df

def select_1csv_line(dataframe, column_name, value) :
    df = dataframe.loc[dataframe[column_name] == value]
    return df

