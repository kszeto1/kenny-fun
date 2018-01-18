import pprint
import requests
import pandas as pd
import matplotlib.pyplot as plt



def get_bls_key():
    """
    This method will get the BLS API key that is expected in api-key.txt file. That file is in the .gitignore and
    each user should have their own API key
    :rtype string
    """
    with open('api-key.txt', 'r') as api_key_file:
        api_key = api_key_file.read()
        return api_key


# Task
coal_series = {'id': 'CEU1021210001',
               'name': 'Number of Coal Employees'}

gas_series = {'id': 'CEU1021100001',
              'name': 'Number of Gas Employees'}

series_id = 'CEU 1021100001'.replace(' ', '')
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data'
api_key = get_bls_key()
r = requests.post(url=url, json={'seriesid': [series_id],
                                 'startyear': '2008',
                                 'endyear': '2017',
                                 'registrationkey': api_key}).json()


r = r['Results']['series'][0]['data']


df = pd.DataFrame(r)
df = df[::-1]
df.index = range(0,120, 1)
df = pd.to_numeric(df['value'])

df.plot()
plt.minorticks_on()
plt.grid(which='both')
plt.ylabel("Number of Employees (in thousands)")
plt.show()

# Goal: Understand that the series id means and graph the output

