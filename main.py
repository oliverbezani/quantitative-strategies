from data import equities_data_fetch as edf
from data import index_ticker_fetch as itf
import pandas as pd
import os
import shutil

def main(): 

    tickers = itf.fetch_index_tickers()

    os.mkdir('temp')
    for ticker in tickers:
        data = edf.yf_fetch_prices(ticker='AAPL', range=100)

        data.to_csv(f'temp/{ticker}.csv')


    shutil.rmtree('temp')


if __name__ == '__main__': main() 