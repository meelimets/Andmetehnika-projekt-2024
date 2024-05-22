# Importing libaries
import pandas as pd

# Reading data file
data=pd.read_csv("DataGBIF_Final.csv")

# Defining columns to keep
columns_to_keep = [
    'gbifID', 'MNIMI', 'MKOOD', 'iso_code', 'kingdom', 'family',
    'genus', 'species', 'locality', 'individualCount', 'decimalLatitude',
    'decimalLongitude', 'eventDate', 'day', 'month', 'year'
]

# Subsetting the data based on columns
subset_df = data[columns_to_keep]

# Saving file as .csv file
subset_df.to_csv('DataGBIF_Final_smallV2.csv', index=False)
