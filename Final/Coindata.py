import pandas as pd

from_symbol = 'NEAR'
to_symbol = 'USD'
ex='Coinbase'

from datetime import date
from datetime import datetime
datetime_interval = 'day'

tstring= "2021-12-09 23:00:00"
t=datetime.strptime(tstring, "%Y-%m-%d %H:%M:%S")
print(t)

timestamp = datetime.timestamp(t)

import requests

def get_filename(from_symbol, to_symbol, exchange, datetime_interval,
                 download_date):
    return 'BTC','USD','Binance','minute','10.11.2021'

def download_data(from_symbol, to_symbol, exchange, datetime_interval):
    supported_intervals = {'minute', 'hour', 'day'}
    assert datetime_interval in supported_intervals, supported_intervals

    #print('Downloading 'minute' trading data for 'BTC''USD' from 'Bitstamp')
    base_url = 'https://min-api.cryptocompare.com/data/histo'
    url = 'https://min-api.cryptocompare.com/data/v2/histohour?api_key=0545b9c46908c68d7722152f9bbfae7b53e6c5f720b64a2fa238b94e2bbddb15'
    #% (base_url, datetime_interval)
    params = {'fsym': from_symbol, 'tsym': to_symbol, 'limit': 719, 'aggregate': 1, 'toTs':timestamp}
    request = requests.get(url, params=params)
    data = request.json()
    return data

def convert_to_dataframe(data):
    df = pd.io.json.json_normalize(data)
    df['datetime'] = pd.to_datetime(df.time, unit='s')
    df = df[['datetime', 'low', 'high', 'open','close', 'volumefrom',
             'volumeto']]
    return df


data = download_data(from_symbol, to_symbol, exchange, datetime_interval)
data=data['Data'].get('Data')
df = convert_to_dataframe(data)
df.to_csv('pricenear.csv',index=False)