import pandas as pd
from pandas import DataFrame

def rsi(prices: DataFrame, window: int = 14):
    delta = prices['Close'].diff()

    gains = delta.where(delta > 0, 0)
    losses = delta.where(delta > 0, 0)

    gains_average = gains.ewm(span = window, min_periods = window).mean()
    losses_average = losses.ewm(span = window, min_periods = window).mean()

    relative_strength = gains_average / losses_average
    relative_strength_index = (100 - (100 / (1 + relative_strength)))

    return relative_strength_index

def sma(prices: DataFrame, window: int = 50):
    simple_moving_average = prices['Close'].rolling(window = window).mean()

    return simple_moving_average

def bollinger_bands(prices: DataFrame, sma_window: int = 20, band_window: int = 20, deviations: int = 2):
    simple_moving_average = prices['Close'].rolling(window = sma_window).mean()
    standard_deviation = prices['Close'].rolling(window = band_window).std()

    upper_band = (simple_moving_average + (deviations * standard_deviation))
    lower_band = (simple_moving_average - (deviations * standard_deviation))

    return simple_moving_average, upper_band, lower_band



