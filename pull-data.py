#!/usr/bin/python

# Import modules
import pandas as pd
import requests
import numpy as np

# Set ipython's max row display
pd.set_option('display.max_row', 1000)

# Insert your CrisisNET API key
api_key = '532d8dc4ed3329652f114b73'

# Insert your CrisisNET request API
api_url = 'http://api.crisis.net/item/?sources=noaa_alerts'

# Create the request header
headers = {'Authorization': 'Bearer ' + api_key}

# Define how many data points you want
total = 10000

# Create a dataframe where the request data will go
df = pd.DataFrame()

# Define a function called get data,
def get_data(offset=0, limit=100, df=None):
    # create a variable called url, which has the request info,
    url = api_url + '&offset=' + str(offset) + '&limit=' + str(limit)
    # a variable called r, with the request data,
    r = requests.get(url, headers=headers)
    # convert the request data into a dataframe,
    x = pd.DataFrame(r.json())
    # expand the dataframe
    x = x['data'].apply(pd.Series)
    # add the dataframe's rows to the main dataframe, df, we defined outside the function
    df = df.append(x, ignore_index=True)

    # then, if the total is larger than the request limit plus offset,
    if total > offset + limit:
        # run the function another time
        return get_data(offset + limit, limit, df)
    # but if not, end the function
    return df

# Run the function
df = get_data(df=df)

# Check the number of data points retrieved
len(df)

# Check for duplicate data points
df['id'].duplicated().value_counts()

# Drop all duplicate data points
df = df.dropna(how='all')

# View the first 10 data points
df.head()


