import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator




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

def create_series_request(series_id):
    series_id = series_id.replace(' ', '')
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

    df['timestamp'] = pd.to_datetime(df['year'] + ' ' + df['periodName'], format="%Y %B")
    df['date_info'] = pd.to_datetime(df['timestamp'])
    df['num_of_employees'] = pd.to_numeric(df['value'])
    return df

coal_request = create_series_request(coal_series['id'])
gas_request = create_series_request(gas_series['id'])

#create x and y values for coal data
coal_employees = []
coal_dates = []

for coal_data in coal_request.iterrows():
    coal_employees.append(float(coal_data[1]['value']))
    coal_dates.append(coal_data[1]['date_info'])

#create x and y values for gas data
gas_employees = []
gas_dates = []
for gas_data in gas_request.iterrows():
    gas_employees.append(float(gas_data[1]['value']))
    gas_dates.append(gas_data[1]['date_info'])

#create figure and subplots
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

#create subplot for coal employees
ax1.plot(coal_dates, coal_employees)
ax1.grid(True)
ax1.set_xlim(coal_dates[0],coal_dates[-1])
minorLocator = AutoMinorLocator(12)
ax1.xaxis.set_minor_locator(minorLocator)
ax1.set_xticklabels([])
ax1.set_title("Number of Coal Employees")
ax1.set_ylabel("Number of employees (in thousands)")

#create subplot for gas employees
ax2.plot(gas_dates, gas_employees)
ax2.grid(True)
ax2.set_xlim(gas_dates[0],gas_dates[-1])
ax2.xaxis.set_minor_locator(minorLocator)
ax2.set_title("Number of Gas Employees")
ax2.set_ylabel("Number of employees (in thousands)")

plt.show()


# Goal: Understand that the series id means and graph the output

