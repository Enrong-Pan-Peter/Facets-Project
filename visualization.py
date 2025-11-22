"""
Visualization Module
--------------------
Functions for creating plots and charts.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_stock_distribution(ST, S0, K, filename='stock_distribution.png'):
    """
    Create histogram of simulated final stock prices.
    
    Parameters
    ----------
    ST : np.ndarray
        Simulated final stock prices
    S0 : float
        Current stock price
    K : float
        Strike price
    filename : str
        Output filename for saving plot
    """
    plt.figure(figsize=(12, 7))
    plt.hist(ST, bins=50, density=True, alpha=0.7, color='steelblue', edgecolor='black')
    
    mean_price = np.mean(ST)
    
    plt.axvline(S0, color='green', linestyle='--', linewidth=2, label=f'Current Price: ${S0:.2f}')
    plt.axvline(K, color='red', linestyle='--', linewidth=2, label=f'Strike Price: ${K:.2f}')
    plt.axvline(mean_price, color='orange', linestyle='--', linewidth=2, label=f'Mean Final Price: ${mean_price:.2f}')
    
    plt.xlabel('Final Stock Price ($)', fontsize=12)
    plt.ylabel('Probability Density', fontsize=12)
    plt.title('Distribution of Simulated AAPL Stock Prices\n(50,000 Monte Carlo Simulations)', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


def plot_convergence(sim_counts, prices, filename='convergence_plot.png'):
    """
    Create plot showing price convergence with simulation count.
    
    Parameters
    ----------
    sim_counts : list
        List of simulation counts
    prices : list
        Corresponding option prices
    filename : str
        Output filename for saving plot
    """
    final_price = prices[-1]
    
    plt.figure(figsize=(12, 7))
    plt.plot(sim_counts, prices, marker='o', linewidth=2, markersize=8, color='darkblue')
    plt.axhline(final_price, color='red', linestyle='--', linewidth=2, 
                label=f'Final Price: ${final_price:.4f}')
    plt.xlabel('Number of Simulations', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Monte Carlo Convergence Analysis\nOption Price Stability vs. Number of Simulations', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


def plot_payoff_distribution(payoffs, filename='payoff_distribution.png'):
    """
    Create histogram of option payoffs.
    
    Parameters
    ----------
    payoffs : np.ndarray
        Array of option payoffs
    filename : str
        Output filename for saving plot
    """
    mean_payoff = np.mean(payoffs)
    zero_payoffs = (payoffs == 0).sum()
    pct_worthless = (zero_payoffs / len(payoffs)) * 100
    
    plt.figure(figsize=(12, 7))
    plt.hist(payoffs, bins=50, alpha=0.7, color='coral', edgecolor='black')
    plt.axvline(mean_payoff, color='darkred', linestyle='--', linewidth=2, 
                label=f'Average Payoff: ${mean_payoff:.2f}')
    
    # Add text box with statistics
    # textstr = f'{pct_worthless:.1f}% of options\nexpire worthless'
    # props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    # plt.text(0.72, 0.95, textstr, transform=plt.gca().transAxes, fontsize=11,
    #          verticalalignment='top', bbox=props)
    
    plt.xlabel('Option Payoff at Expiration ($)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Distribution of Call Option Payoffs\nStrike Price: ${:.2f}'.format(mean_payoff), 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


def plot_validation_comparison(strikes, mc_prices, market_prices, filename='validation_comparison.png'):
    """
    Create comparison plot of Monte Carlo vs market prices.
    
    Parameters
    ----------
    strikes : list
        Strike prices
    mc_prices : list
        Monte Carlo option prices
    market_prices : list
        Real market option prices
    filename : str
        Output filename for saving plot
    """
    plt.figure(figsize=(10, 6))
    x = np.arange(len(strikes))
    width = 0.35
    
    plt.bar(x - width/2, mc_prices, width, label='Monte Carlo Price', color='steelblue', alpha=0.8)
    plt.bar(x + width/2, market_prices, width, label='Market Price', color='coral', alpha=0.8)
    
    plt.xlabel('Strike Price ($)', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Monte Carlo vs Market Prices - Validation', fontsize=14, fontweight='bold')
    plt.xticks(x, strikes)
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


def plot_sensitivity_volatility(volatilities, prices, filename='volatility_sensitivity.png'):
    """
    Plot how option price changes with volatility.
    
    Parameters
    ----------
    volatilities : list
        Volatility values
    prices : list
        Corresponding option prices
    filename : str
        Output filename for saving plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(volatilities, prices, marker='o', linewidth=2, markersize=8, color='darkgreen')
    plt.xlabel('Volatility (σ)', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Effect of Volatility on Option Price', fontsize=14, fontweight='bold')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


def plot_sensitivity_strike(strikes, prices, S0, filename='strike_sensitivity.png'):
    """
    Plot how option price changes with strike price.
    
    Parameters
    ----------
    strikes : list
        Strike prices
    prices : list
        Corresponding option prices
    S0 : float
        Current stock price
    filename : str
        Output filename for saving plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(strikes, prices, marker='o', linewidth=2, markersize=8, color='darkblue')
    plt.axvline(S0, color='red', linestyle='--', linewidth=2, label=f'Current Price: ${S0:.2f}')
    plt.xlabel('Strike Price ($)', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Effect of Strike Price on Option Price', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
