import numpy as np
import tensorflow as tf 
from keras.models import Sequential
from keras.layers import Input, LSTM, Dense, Dropout, Bidirectional, Conv1D, MaxPooling1D, Flatten, Attention
from keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def lstm(prices, n_steps = 25): 
    n_features = prices.shape[1]
    
    X_train, X_test, y_train, y_test = preprocessing(prices, n_steps, n_features)

    model = Sequential([
    Input(shape=(n_steps, n_features)),
    Conv1D(filters=64, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Dropout(0.2),
    Bidirectional(LSTM(50, return_sequences=True)),
#     Attention(),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
    ])

    model.compile(optimizer=Adam(), loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print('MSE: ', mse)



def preprocessing(prices, n_steps, n_features): 
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalised_prices = scaler.fit_transform(prices.values)

    X, y = [], []
    for i in range(len(normalised_prices) - n_steps):
        X.append(normalised_prices[i:i+n_steps, :])
        y.append(normalised_prices[i+n_steps, 0])

    X, y = np.array(X), np.array(y)

    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], n_features))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], n_features))

    return X_train, X_test, y_train, y_test
