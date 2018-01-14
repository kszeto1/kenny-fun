import pprint
import requests


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
series_id = 'CE U 08000000 01'.replace(' ', '')
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data'
api_key = get_bls_key()
r = requests.post(url=url, json={'seriesid': [series_id],
                                 'startyear': '2014',
                                 'endyear': '2017',
                                 'registrationkey': api_key})
pprint.pprint(r.json())

# Goal: Understand that the series id means and graph the output

