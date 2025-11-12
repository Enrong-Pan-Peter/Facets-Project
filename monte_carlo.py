"""
Core Monte Carlo simulation for European Call Options
"""

import numpy as np
import yfinance as yf # for fetching real stock data
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# set random seed for reproducibility
np.random.seed(42)


def monte_carlo_option(S0, K, T, r, sigma, num_sims=50000, option_type='call'):
    """
    Price a European option using Monte Carlo simulation.
    
    Parameters:
    S0 : float -> current stock price
    K : float -> strike price
    T : float -> time to maturity (in years) aka how long until expiration
    r : float -> risk-free interest rate (annualized)
    sigma : float -> volatility (annualized)
    num_sims : int -> number of Monte Carlo simulations
    option_type : str -> 'call' or 'put'
    
    Returns:
    option_price : float -> estimated option price
    ST : ndarray -> array of simulated final stock prices
    payoffs : ndarray -> array of option payoffs
    """
    
    # generate random standard normal variables
    Z = np.random.standard_normal(num_sims)
    
    # simulate final stock prices using Geometric Brownian Motion
    # formula: ST = S0 * exp((r - 0.5*sigma^2)*T + sigma*sqrt(T)*Z)
    # we will include this formula in our poster
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # calculate payoffs based on option type
    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)  # call payoff: max(ST - K, 0)
    else:  # put
        payoffs = np.maximum(K - ST, 0)  # put payoff: max(K - ST, 0)
    
    # discount payoffs to present value
    option_price = np.exp(-r * T) * np.mean(payoffs)
    
    return option_price, ST, payoffs


def get_stock_data(ticker='AAPL', period='1y'):
    """
    fetch historical stock data and calculate volatility.
    
    Parameters:
    ticker : str -> stock ticker symbol
    period : str -> time period for historical data
    
    Returns:
    dict containing:
        - current_price: current stock price
        - volatility: historical volatility (annualized)
        - hist_data: dataFrame of historical prices
    """
    
    print(f"Fetching data for {ticker}...")
    
    # download stock data
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    
    if hist.empty:
        raise ValueError(f"No data found for {ticker}")
    
    # calculate daily returns
    hist['Returns'] = np.log(hist['Close'] / hist['Close'].shift(1))
    
    # calculate annualized volatility
    # formula: σ_annual = σ_daily * sqrt(252)
    # 252 is the number of trading days in a year
    daily_volatility = hist['Returns'].std()
    annual_volatility = daily_volatility * np.sqrt(252)
    
    # get current price
    current_price = hist['Close'].iloc[-1]
    
    print(f"Current {ticker} price: ${current_price:.2f}")
    print(f"Historical volatility: {annual_volatility:.3f} ({annual_volatility*100:.1f}%)")
    
    return {
        'current_price': current_price,
        'volatility': annual_volatility,
        'hist_data': hist,
        'ticker': ticker
    }


def convergence_analysis(S0, K, T, r, sigma, max_sims=50000):
    """
    show how option price converges as we increase number of simulations.
    
    Returns:
    sim_counts : list -> number of simulations used
    prices : list -> option prices at each simulation count
    """
    
    sim_counts = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    prices = []
    
    print("\nConvergence Analysis:")
    print("-" * 50)
    
    for n in sim_counts:
        price, _, _ = monte_carlo_option(S0, K, T, r, sigma, num_sims=n)
        prices.append(price)
        print(f"Simulations: {n:6d} | Option Price: ${price:.4f}")
    
    return sim_counts, prices

# this function creates all three required visualizations, it is optional to take a look at it, you don't need to understand every line
def create_visualizations(ST, payoffs, sim_counts, prices, 
                         option_price, S0, K, ticker):
    """
    Create all three required visualizations.
    """
    
    # Set style for better-looking plots
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Figure 1: Stock Price Distribution
    print("  Creating Figure 1: Stock Price Distribution...")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.hist(ST, bins=100, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    ax1.axvline(S0, color='green', linestyle='--', linewidth=2, label=f'Current Price: ${S0:.2f}')
    ax1.axvline(K, color='red', linestyle='--', linewidth=2, label=f'Strike Price: ${K:.2f}')
    ax1.axvline(np.mean(ST), color='orange', linestyle='--', linewidth=2, 
                label=f'Mean Final Price: ${np.mean(ST):.2f}')
    
    ax1.set_xlabel('Final Stock Price ($)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Probability Density', fontsize=12, fontweight='bold')
    ax1.set_title(f'Distribution of Simulated {ticker} Stock Prices\n(50,000 Monte Carlo Simulations)', 
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('stock_price_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Figure 2: Convergence Plot
    print("  Creating Figure 2: Convergence Plot...")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    ax2.plot(sim_counts, prices, marker='o', linewidth=2, markersize=8, color='darkblue')
    ax2.axhline(option_price, color='red', linestyle='--', linewidth=2, 
                label=f'Final Price: ${option_price:.4f}')
    
    ax2.set_xlabel('Number of Simulations', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Option Price ($)', fontsize=12, fontweight='bold')
    ax2.set_title('Monte Carlo Convergence Analysis\nOption Price Stability vs. Number of Simulations', 
                  fontsize=14, fontweight='bold')
    ax2.set_xscale('log')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('convergence_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Figure 3: Payoff Distribution
    print("  Creating Figure 3: Payoff Distribution...")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    
    ax3.hist(payoffs, bins=100, alpha=0.7, color='lightcoral', edgecolor='black')
    ax3.axvline(np.mean(payoffs), color='darkred', linestyle='--', linewidth=2, 
                label=f'Average Payoff: ${np.mean(payoffs):.2f}')
    
    # Add text showing percentage with zero payoff
    zero_payoff_pct = (np.sum(payoffs == 0) / len(payoffs)) * 100
    ax3.text(0.98, 0.95, f'{zero_payoff_pct:.1f}% of options\nexpire worthless', 
             transform=ax3.transAxes, fontsize=11, verticalalignment='top',
             horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax3.set_xlabel('Option Payoff at Expiration ($)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax3.set_title(f'Distribution of Call Option Payoffs\nStrike Price: ${K:.2f}', 
                  fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('payoff_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()


def main():

    print("Monte Carlo Option Pricing - Core Implementation")
    
    # get real stock data
    stock_data = get_stock_data('AAPL', period='1y')
    
    # set parameters
    S0 = stock_data['current_price']  # current stock price
    K = round(S0, 0)  # strike price (at-the-money, rounded)
    T = 0.25  # 3 months = 0.25 years
    r = 0.045  # 4.5% risk-free rate (approximate current US Treasury rate)
    sigma = stock_data['volatility']  # historical volatility
    num_sims = 50000  # number of simulations
    
    print("\n")
    print("Parameters:")
    print(f"Stock: {stock_data['ticker']}")
    print(f"Current Price (S0): ${S0:.2f}")
    print(f"Strike Price (K): ${K:.2f}")
    print(f"Time to Maturity (T): {T} years ({T*12:.0f} months)")
    print(f"Risk-free Rate (r): {r:.3f} ({r*100:.1f}%)")
    print(f"Volatility (σ): {sigma:.3f} ({sigma*100:.1f}%)")
    print(f"Number of Simulations: {num_sims:,}")
    print("\n")
    
    # run Monte Carlo simulation
    print("Running Monte Carlo Simulation...")
    
    option_price, ST, payoffs = monte_carlo_option(
        S0, K, T, r, sigma, num_sims, option_type='call'
    )
    
    print("\n")
    print(f"\n✓ Simulation Complete!")
    print(f"European Call Option Price: ${option_price:.4f}")
    print("\n")
    
    # calculate some statistics
    avg_final_price = np.mean(ST)
    std_final_price = np.std(ST)
    prob_in_money = np.mean(ST > K) * 100
    
    print("\n")
    print(f"\nSimulation Statistics:")
    print(f"  Average Final Stock Price: ${avg_final_price:.2f}")
    print(f"  Std Dev of Final Prices: ${std_final_price:.2f}")
    print(f"  Probability of Finishing In-The-Money: {prob_in_money:.1f}%")
    print("\n")
    
    # convergence analysis
    sim_counts, prices = convergence_analysis(S0, K, T, r, sigma)
    
    # create visualizations
    print("\n")
    print("Generating Visualizations...")
    print("\n")
    
    create_visualizations(
        ST, payoffs, sim_counts, prices, 
        option_price, S0, K, stock_data['ticker']
    )
    
    print("\nFiles created:")
    print("  1. monte_carlo.py (this file)")
    print("  2. stock_price_distribution.png")
    print("  3. convergence_plot.png")
    print("  4. payoff_distribution.png")
    
    return {
        'option_price': option_price,
        'parameters': {
            'S0': S0, 'K': K, 'T': T, 'r': r, 'sigma': sigma
        },
        'statistics': {
            'avg_final_price': avg_final_price,
            'std_final_price': std_final_price,
            'prob_in_money': prob_in_money
        }
    }

if __name__ == "__main__":
    results = main()

    """
    parameters for @Henry:
    S0 = 185.40
    K = 185.00
    T = 0.25
    r = 0.045
    sigma = 0.283
    """
    
    """
    code snippit for @Jiayi:
    
    from monte_carlo_demo import monte_carlo_option

    # 测试不同volatility
    for sigma in [0.2, 0.25, 0.3, 0.35, 0.4]:
        price, _, _ = monte_carlo_option(185.40, 185.00, 0.25, 0.045, sigma)
        print(f"σ={sigma}: ${price:.2f}")
    """