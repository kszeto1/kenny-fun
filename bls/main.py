import arrow
import pprint
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import datetime



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

date1 = arrow.get(2008, 1, 1)
date2 = arrow.get(2017, 12, 1)

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

    # df['date_info'] = pd.to_datetime(df['year'] + ' ' + df['periodName'], format="%Y %B")
    df['num_of_employees'] = pd.to_numeric(df['value'])
    return df

coal_request = create_series_request(coal_series['id'])
gas_request = create_series_request(gas_series['id'])

coal_employees = []
coal_dates = []
# print('coal_request:',coal_request)
for i, coal_data in enumerate(coal_request.iterrows()):
    # print('coal_data values:',coal_data[1]['value'])
    coal_employees.append(float(coal_data[1]['value']))
    coal_dates.append(date1.shift(months=i).datetime)
print("coal employees:", coal_employees)
print("coal dates:", coal_dates)

# gas_employees = []
# gas_dates = []
# for date in gas_request:
#     gas_employees.append(float(gas_request['value']))
#     gas_dates.append(gas_request['date_info'])

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)


ax1.plot(coal_dates, coal_employees, 'Number of Coal Employees')
fig.autofmt_xdate()
# ax2.plot(gas_dates, gas_employees, 'Number of Gas Employees')


# df.plot(x='date_info', y='num_of_employees')
# fig, axarr = plt.subplots(2, sharex=True)
# axarr[0].plot(x, y)
# plt.ylabel("Number of Employees (in thousands)")
# plt.grid(True)
# months = range(0, 12, 1)
# multiple_loc = MultipleLocator(1)
# plt.axes().xaxis.set_minor_locator(multiple_loc)
plt.show()


# Goal: Understand that the series id means and graph the output

