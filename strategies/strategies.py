from data import equities_data_fetch as edf
from data import index_ticker_fetch as itf
from indicators import indicators as ind
from models import lstm
from optimisers import optimisers as opt

def sp500_top_10(capital: int): 

    tickers = itf.fetch_index_tickers()
    predicted_closes = {}

    for ticker in tickers:
        data = edf.yf_fetch_prices(ticker=ticker, range=500)

        data.to_csv(f'temp/{ticker}.csv')

        data['RSI'] = ind.rsi(data)
        data['Middle'], data['Upper'], data['Lower'] = ind.bollinger_bands(data)
        data['SMA_50'] = ind.sma(data)
        data.dropna(inplace=True)

        predicted_close = lstm.lstm(data)
        predicted_closes[ticker] = predicted_close

    positive_predicted_closes = {t: r for t, r in predicted_closes.items() if r > 0}
    sorted_predicted_closes = sorted(positive_predicted_closes.items(), key=lambda item: item[1], reverse=True)
    top_10_predictions = dict(sorted_predicted_closes[:10])

    ticker_allocations = opt.slsqp(top_10_predictions, capital)

    return ticker_allocations