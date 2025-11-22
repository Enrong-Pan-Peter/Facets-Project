"""
Person 4: Sensitivity Analysis
-------------------------------
Analyze how different parameters affect option prices.
"""

import numpy as np
from data_fetcher import get_stock_parameters
from monte_carlo import price_option
from visualization import plot_sensitivity_volatility, plot_sensitivity_strike


def main():
    """Run Person 4's sensitivity analysis."""
    
    print("=" * 60)
    print("Person 4: Parameter Sensitivity Analysis")
    print("=" * 60)
    
    # Get base parameters
    print("\nFetching base parameters...")
    stock_params = get_stock_parameters('AAPL')
    S0 = stock_params['current_price']
    sigma_base = stock_params['volatility']
    
    K = 274.00
    T = 0.25
    r = 0.045
    
    print(f"Base Parameters:")
    print(f"  Current Price: ${S0:.2f}")
    print(f"  Base Volatility: {sigma_base:.3f}")
    print(f"  Strike: ${K:.2f}")
    
    # Analysis 1: Volatility Sensitivity
    print("\n" + "=" * 60)
    print("Analysis 1: Volatility Sensitivity")
    print("=" * 60)
    
    volatilities = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
    vol_prices = []
    
    print("\nTesting different volatility levels...")
    for vol in volatilities:
        price, _, _ = price_option(S0, K, T, r, vol, num_sims=10000)
        vol_prices.append(price)
        print(f"Volatility {vol:.2f} ({vol*100:.0f}%): Option Price = ${price:.2f}")
    
    plot_sensitivity_volatility(volatilities, vol_prices, 'person4_volatility_sensitivity.png')
    print("\nCreated: person4_volatility_sensitivity.png")
    
    # Analysis 2: Strike Price Sensitivity
    print("\n" + "=" * 60)
    print("Analysis 2: Strike Price Sensitivity")
    print("=" * 60)
    
    strikes = [260, 265, 270, 275, 280, 285, 290]
    strike_prices = []
    
    print("\nTesting different strike prices...")
    for strike in strikes:
        price, _, _ = price_option(S0, strike, T, r, sigma_base, num_sims=10000)
        strike_prices.append(price)
        print(f"Strike ${strike:.2f}: Option Price = ${price:.2f}")
    
    plot_sensitivity_strike(strikes, strike_prices, S0, 'person4_strike_sensitivity.png')
    print("\nCreated: person4_strike_sensitivity.png")
    
    # Summary
    print("\n" + "=" * 60)
    print("Key Findings:")
    print("=" * 60)
    print("\n1. Volatility Impact:")
    print("   - Higher volatility increases option prices")
    print(f"   - At σ=0.10: ${vol_prices[0]:.2f}")
    print(f"   - At σ=0.40: ${vol_prices[-1]:.2f}")
    print(f"   - Price increase: {((vol_prices[-1]/vol_prices[0])-1)*100:.1f}%")
    
    print("\n2. Strike Price Impact:")
    print("   - Lower strikes give higher call option prices")
    print(f"   - At K=${strikes[0]}: ${strike_prices[0]:.2f}")
    print(f"   - At K=${strikes[-1]}: ${strike_prices[-1]:.2f}")
    
    print("\n" + "=" * 60)
    print("Person 4 work completed successfully!")
    print("=" * 60)
    print("\nFiles created:")
    print("1. person4_volatility_sensitivity.png")
    print("2. person4_strike_sensitivity.png")


if __name__ == "__main__":
    main()
