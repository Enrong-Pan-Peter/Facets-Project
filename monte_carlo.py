"""
Monte Carlo Simulation Module
------------------------------
Core functions for Monte Carlo option pricing.
"""

import numpy as np


def generate_random_paths(num_sims=50000):
    """
    Generate random standard normal variables for simulation.
    
    Parameters
    ----------
    num_sims : int
        Number of simulation paths
    
    Returns
    -------
    np.ndarray
        Array of random standard normal variables
    """
    np.random.seed(42)
    return np.random.standard_normal(num_sims)


def simulate_stock_prices(S0, T, r, sigma, random_paths):
    """
    Simulate final stock prices using Geometric Brownian Motion.
    
    Parameters
    ----------
    S0 : float
        Current stock price
    T : float
        Time to maturity in years
    r : float
        Risk-free interest rate
    sigma : float
        Volatility (annualized)
    random_paths : np.ndarray
        Random standard normal variables
    
    Returns
    -------
    np.ndarray
        Simulated final stock prices
    """
    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T) * random_paths
    ST = S0 * np.exp(drift + diffusion)
    return ST


def calculate_call_payoffs(ST, K):
    """
    Calculate call option payoffs.
    
    Parameters
    ----------
    ST : np.ndarray
        Final stock prices
    K : float
        Strike price
    
    Returns
    -------
    np.ndarray
        Option payoffs for each simulated price
    """
    return np.maximum(ST - K, 0)


def calculate_put_payoffs(ST, K):
    """
    Calculate put option payoffs.
    
    Parameters
    ----------
    ST : np.ndarray
        Final stock prices
    K : float
        Strike price
    
    Returns
    -------
    np.ndarray
        Option payoffs for each simulated price
    """
    return np.maximum(K - ST, 0)


def discount_to_present(payoffs, r, T):
    """
    Discount future payoffs to present value.
    
    Parameters
    ----------
    payoffs : np.ndarray
        Future option payoffs
    r : float
        Risk-free interest rate
    T : float
        Time to maturity in years
    
    Returns
    -------
    float
        Present value of option
    """
    return np.exp(-r * T) * np.mean(payoffs)


def price_option(S0, K, T, r, sigma, num_sims=50000, option_type='call'):
    """
    Price a European option using Monte Carlo simulation.
    
    Parameters
    ----------
    S0 : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity in years
    r : float
        Risk-free interest rate
    sigma : float
        Volatility (annualized)
    num_sims : int
        Number of simulations
    option_type : str
        'call' or 'put'
    
    Returns
    -------
    tuple
        (option_price, simulated_prices, payoffs)
    """
    random_paths = generate_random_paths(num_sims)
    ST = simulate_stock_prices(S0, T, r, sigma, random_paths)
    
    if option_type == 'call':
        payoffs = calculate_call_payoffs(ST, K)
    else:
        payoffs = calculate_put_payoffs(ST, K)
    
    option_price = discount_to_present(payoffs, r, T)
    
    return option_price, ST, payoffs


def analyze_convergence(S0, K, T, r, sigma, sim_counts):
    """
    Analyze how option price converges with increasing simulations.
    
    Parameters
    ----------
    S0 : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity in years
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    sim_counts : list
        List of simulation counts to test
    
    Returns
    -------
    list
        Option prices at each simulation count
    """
    prices = []
    for n in sim_counts:
        price, _, _ = price_option(S0, K, T, r, sigma, num_sims=n)
        prices.append(price)
    return prices
