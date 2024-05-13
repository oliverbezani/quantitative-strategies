from data import equities_data_fetch as edf
from data import index_ticker_fetch as itf
from indicators import indicators as ind
from models import lstm
import pandas as pd
import os
import shutil

def main(): 

    tickers = ['AAPL']# itf.fetch_index_tickers()

    if os.path.exists('temp'):
            shutil.rmtree('temp')
    os.mkdir('temp')

    for ticker in tickers:
        data = edf.yf_fetch_prices(ticker='AAPL', range=500)

        data['RSI'] = ind.rsi(data)
        data['Middle'], data['Upper'], data['Lower'] = ind.bollinger_bands(data)
        data['SMA_50'] = ind.sma(data)
        data.dropna(inplace=True)

        lstm.lstm(data)

        data.to_csv(f'temp/{ticker}.csv')



if __name__ == '__main__': main() 