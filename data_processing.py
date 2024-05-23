import pandas as pd

def read_csv_files(file_path) :
    df = pd.read_csv(file_path)
    return df

def select_csv_line(dataframe, column_name, value) :
    df = dataframe.loc[dataframe[column_name] == value]
    return df

def select_csv_column(dataframe, column_name) :
    df = dataframe[column_name]
    return df


def select_between_csv_line(dataframe, column_name, value1, value2):
    # Validate parameters
    if value1 is None and value2 is None:
        raise ValueError("At least one value must be provided.")

    # Swap values if necessary
    if value1 is not None and value2 is not None and value1 > value2:
        value1, value2 = value2, value1

    # Handle edge cases and select rows based on the range
    if value1 == value2:
        return select_csv_line(dataframe, column_name, value1)
    elif value1 is None:
        return dataframe.loc[dataframe[column_name] < value2]
    elif value2 is None:
        return dataframe.loc[dataframe[column_name] > value1]
    else:
        return dataframe.loc[(dataframe[column_name] > value1) & (dataframe[column_name] < value2)]

