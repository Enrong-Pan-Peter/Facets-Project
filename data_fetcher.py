"""
Data Fetching Module
--------------------
Functions for fetching and processing stock market data.
"""

import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def fetch_stock_history(ticker='AAPL', period='1y'):
    """
    Fetch historical stock price data.
    
    Parameters
    ----------
    ticker : str
        Stock ticker symbol (default: 'AAPL')
    period : str
        Time period for historical data (default: '1y')
    
    Returns
    -------
    pd.DataFrame
        Historical stock prices with Date, Open, High, Low, Close, Volume
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist


def get_current_price(ticker='AAPL'):
    """
    Get the current stock price.
    
    Parameters
    ----------
    ticker : str
        Stock ticker symbol
    
    Returns
    -------
    float
        Current stock price
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period='1d')
    return hist['Close'].iloc[-1]


def calculate_volatility(price_history):
    """
    Calculate annualized historical volatility from price data.
    
    Parameters
    ----------
    price_history : pd.DataFrame
        DataFrame with 'Close' column containing historical prices
    
    Returns
    -------
    float
        Annualized volatility (sigma)
    """
    returns = np.log(price_history['Close'] / price_history['Close'].shift(1))
    daily_volatility = returns.std()
    annualized_volatility = daily_volatility * np.sqrt(252)
    return annualized_volatility


def get_stock_parameters(ticker='AAPL'):
    """
    Get all parameters needed for option pricing from stock data.
    
    Parameters
    ----------
    ticker : str
        Stock ticker symbol
    
    Returns
    -------
    dict
        Dictionary with keys: 'current_price', 'volatility', 'ticker'
    """
    history = fetch_stock_history(ticker)
    current_price = get_current_price(ticker)
    volatility = calculate_volatility(history)
    
    return {
        'ticker': ticker,
        'current_price': current_price,
        'volatility': volatility
    }
