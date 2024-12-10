import pandas as pd

def print_unique_values(data: pd.DataFrame):
    columns = data.columns
    for column in columns:
        print(column, ":", data[column].unique())

def preprocess(data: pd.DataFrame):

    # drop duplicates if any
    data.drop_duplicates(inplace=True)

    # correcting auto traffic sigl to auto traffic signal in junction control column
    data["Junction_Control"] = data["Junction_Control"].str.replace("Auto traffic sigl", "Auto traffic signal")

    # correcting fetal to fatal in accident severity
    data["Accident_Severity"] = data["Accident_Severity"].str.replace("Fetal", "Fatal")

    # replacing null value in road surface condition column to Not Available
    data["Road_Surface_Conditions"].fillna("Not Available", inplace=True)

    # replacing null value in road type column to Not Available
    data["Road_Type"].fillna("Not Available", inplace=True)

    # replacing null value in weather conditions column to Not Available
    data["Weather_Conditions"].fillna("Not Available", inplace=True)

    # Light_Conditions
    # ['Daylight' 'Darkness - lights lit' 'Darkness - lighting unknown'
    #  'Darkness - lights unlit' 'Darkness - no lighting']

    # Vehicle_Type
    return data