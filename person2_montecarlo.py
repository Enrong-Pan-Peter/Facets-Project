"""
Person 2: Core Monte Carlo Implementation
------------------------------------------
Main script for running Monte Carlo option pricing with real AAPL data.
"""

import numpy as np
from data_fetcher import get_stock_parameters
from monte_carlo import price_option, analyze_convergence
from visualization import plot_stock_distribution, plot_convergence, plot_payoff_distribution


def main():
    """Run Person 2's Monte Carlo implementation."""
    
    print("=" * 60)
    print("Person 2: Monte Carlo Option Pricing - Core Implementation")
    print("=" * 60)
    
    # Step 1: Fetch real AAPL data
    print("\nStep 1: Fetching AAPL stock data...")
    stock_params = get_stock_parameters('AAPL')
    S0 = stock_params['current_price']
    sigma = stock_params['volatility']
    
    print(f"Current AAPL Price: ${S0:.2f}")
    print(f"Historical Volatility: {sigma:.3f} ({sigma*100:.1f}%)")
    
    # Step 2: Set option parameters
    print("\nStep 2: Setting option parameters...")
    K = 274.00  # Strike price (at-the-money)
    T = 0.25    # 3 months to expiration
    r = 0.045   # Risk-free rate (4.5%)
    num_sims = 50000
    
    print(f"Strike Price: ${K:.2f}")
    print(f"Time to Maturity: {T:.2f} years (3 months)")
    print(f"Risk-free Rate: {r:.3f} ({r*100:.1f}%)")
    print(f"Number of Simulations: {num_sims:,}")
    
    # Step 3: Run Monte Carlo simulation
    print("\nStep 3: Running Monte Carlo simulation...")
    option_price, ST, payoffs = price_option(S0, K, T, r, sigma, num_sims)
    
    print(f"\nOption Price: ${option_price:.2f}")
    print(f"Average Final Stock Price: ${np.mean(ST):.2f}")
    print(f"Standard Deviation: ${np.std(ST):.2f}")
    print(f"In-The-Money Probability: {(ST > K).sum() / len(ST) * 100:.1f}%")
    
    # Step 4: Convergence analysis
    print("\nStep 4: Analyzing convergence...")
    sim_counts = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    convergence_prices = analyze_convergence(S0, K, T, r, sigma, sim_counts)
    
    print("\nConvergence Analysis:")
    print("-" * 60)
    for n, p in zip(sim_counts, convergence_prices):
        print(f"Simulations: {n:6d} | Option Price: ${p:.2f}")
    
    # Step 5: Generate visualizations
    print("\nStep 5: Generating visualizations...")
    plot_stock_distribution(ST, S0, K, 'person2_stock_distribution.png')
    print("Created: person2_stock_distribution.png")
    
    plot_convergence(sim_counts, convergence_prices, 'person2_convergence.png')
    print("Created: person2_convergence.png")
    
    plot_payoff_distribution(payoffs, 'person2_payoff_distribution.png')
    print("Created: person2_payoff_distribution.png")
    
    print("\n" + "=" * 60)
    print("Person 2 work completed successfully!")
    print("=" * 60)
    print("\nFiles created:")
    print("1. person2_stock_distribution.png")
    print("2. person2_convergence.png")
    print("3. person2_payoff_distribution.png")
    print("\nShare these with Person 3 and Person 4 for their work.")


if __name__ == "__main__":
    main()
