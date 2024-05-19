import numpy as np
import pandas as pd
from scipy.optimize import minimize

def slsqp(ticker_returns: dict, capital: int):

    historical_closes = {}
    for ticker in ticker_returns.keys():
        df = pd.read_csv(f'temp/{ticker}.csv')
        historical_closes[ticker] = df['Close']

    historical_closes_df = pd.DataFrame(historical_closes)
    historical_returns_df = historical_closes_df.pct_change().dropna()

    covariance_matrix = historical_returns_df.cov()
    predicted_returns = np.array(list(ticker_returns.values()))

    num_stocks = len(predicted_returns)
    initial_weights = np.ones(num_stocks) / num_stocks
    max_weight = 0.3

    constraints = [{'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
                   {'type': 'ineq', 'fun': lambda weights: max_weight - weights}]
    bounds = [(0, 1) for _ in range(num_stocks)]

    risk_aversion = 10  # Adjust risk aversion parameter
    result = minimize(objective_function, initial_weights, args=(predicted_returns, covariance_matrix.values, risk_aversion),
                    method='SLSQP', bounds=bounds, constraints=constraints)
    
    optised_weights = result.x
    allocations = optised_weights * capital

    ticker_allocations = {ticker: round(allocations[i], 2) for i, ticker in enumerate(ticker_returns.keys())}

    return ticker_allocations

def portfolio_variance(weights: np.ndarray, cov_matrix: np.ndarray):
    return weights.T @ cov_matrix @ weights

def portfolio_return(weights: np.ndarray, exp_returns: np.ndarray):
    return weights.T @ exp_returns

def objective_function(weights: np.ndarray, exp_returns: np.ndarray, cov_matrix: np.ndarray, risk_aversion: float):
    return -portfolio_return(weights, exp_returns) + risk_aversion * portfolio_variance(weights, cov_matrix)


