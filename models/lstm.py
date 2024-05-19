import numpy as np
import tensorflow as tf 
from keras.models import Model, Sequential
from keras.layers import Input, LSTM, Dense, Dropout, Bidirectional, Conv1D, MaxPooling1D
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from pandas import DataFrame, Series
from sklearn.base import TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def lstm(prices: DataFrame, n_steps: int = 25): 
    n_features = prices.shape[1]
    
    X_train, X_test, y_train, y_test, scaler = preprocessing(prices, n_steps, n_features)

    model = Sequential([
    Input(shape=(n_steps, n_features)),
    Conv1D(filters=64, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Dropout(0.2),
    Bidirectional(LSTM(50, return_sequences=True)),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
    ])

    model.compile(optimizer=Adam(), loss='mean_squared_error')
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    model.fit(X_train, 
              y_train, 
              epochs=100, 
              batch_size=32, 
              validation_data=(X_test, y_test), 
              callbacks=[early_stopping], 
              verbose=0)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print('MSE: ', mse)

    next_close_pred = prediction(model, prices[-n_steps:], scaler)

    predicted_return = returns(prices.iloc[-1,0], next_close_pred)

    return round(predicted_return,4)

def preprocessing(prices: DataFrame, n_steps: int, n_features: int): 
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

    return X_train, X_test, y_train, y_test, scaler

def prediction(model: Model, X_pred: Series, scaler: TransformerMixin):
    X_pred_scaled = scaler.transform(X_pred)
    X_pred_scaled = np.reshape(X_pred_scaled, (1, X_pred_scaled.shape[0], X_pred_scaled.shape[1]))

    pred_scaled = model.predict(X_pred_scaled)

    dummy_col_count = X_pred.shape[1] - pred_scaled.shape[1]
    dummy_cols = np.zeros((pred_scaled.shape[0], dummy_col_count))
    pred_scaled_inversion = np.hstack((pred_scaled, dummy_cols))

    pred = scaler.inverse_transform(pred_scaled_inversion)[:,0]

    return pred[0]

def returns(current: float, prediction: float):
    return ((prediction - current)/current)
 
