from vault.api_keys import alpha_vantage

from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf

import datetime
import pandas as pd

def av_fetch_prices(ticker, range, api_key=alpha_vantage, output_format='pandas'):
    ts = TimeSeries(key=api_key, output_format=output_format)

    data, meta_data = ts.get_daily(symbol=ticker)

    data_range = data.head(range)

    return data_range.iloc[::-1]


def yf_fetch_prices(ticker, range):

    yf_ticker = yf.Ticker(ticker)
    data = yf_ticker.history(period=f'{range}d')

    data_close_volume = pd.DataFrame(data[['Close', 'Volume']])
    data_close_volume.set_index(data_close_volume.index.date, inplace=True)

    return data_close_volume




