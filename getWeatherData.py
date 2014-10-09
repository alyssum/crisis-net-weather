#!/usr/bin/python
from microsofttranslator import Translator
import goslate
# Import modules
import pandas as pd
import requests
import numpy as np

# Set ipython's max row display
pd.set_option('display.max_row', 1000)

# Insert your CrisisNET API key
api_key = '532d8dc4ed3329652f114b73'

# Insert your CrisisNET request API
api_url = 'http://api.crisis.net/item?apikey=532d8dc4ed3329652f114b73&sources=twitter&weather,disaster'

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

def run(data):
    if 'language' in data and 'code' in data['language'] and data['language']['code'] == 'en':
        return data


    """
    translator = Translator(settings.BING_APP_ID, settings.BING_APP_SECRET)

    try:
        data['contentEnglish'] = translator.translate(data['content'], "en")
    except Exception, e:
        print e
        pass
    """

    try:
      gs = goslate.Goslate()
      data['contentEnglish'] = gs.translate(data['content'][:1000], 'en')
    except Exception, e:
      print e
      pass

    return data

# Check the number of data points retrieved
len(df)

translated_df=run(df)
print translated_df.head()

# Check for duplicate data points
translated_df['id'].duplicated().value_counts()

# Drop all duplicate data points
translated_df = translated_df.dropna(how='all')

translated_df.to_csv('TwitterWeather.csv',encoding='utf-8')

# View the first 10 data points
#print df.head()
print df['id'].duplicated().value_counts()
print len(df)

translated_df = translated_df.dropna(how='all')
