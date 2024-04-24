from vault.api_keys import alpha_vantage

from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import os
import pandas as pd
import requests


def fetch_prices(ticker, start_date, end_date, api_key=alpha_vantage, output_format='pandas'):
    ts = TimeSeries(key=api_key, output_format=output_format)

    data, meta_data = ts.get_daily(symbol=ticker)

    # ts.get_daily()
    return data 
