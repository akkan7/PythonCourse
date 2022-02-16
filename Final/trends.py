import pandas as pd
import pytrends
from pytrends.request import TrendReq
pytrends = TrendReq()

words=['Shiba']
pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25))
h = pytrend.get_historical_interest(words, year_start=2021, month_start=11, day_start=10, hour_start=0, year_end=2021, month_end=12, day_end=9, hour_end=23, cat=0, geo='', gprop='', sleep=0)
h.to_csv('googleshiba.csv')

words=['near coin']
pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25))
h = pytrend.get_historical_interest(words, year_start=2021, month_start=11, day_start=10, hour_start=0, year_end=2021, month_end=12, day_end=9, hour_end=23, cat=0, geo='', gprop='', sleep=0)
h.to_csv('googlenear.csv')



