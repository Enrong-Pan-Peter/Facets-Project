"""
Person 3: Market Data Validation
---------------------------------
Compare Monte Carlo prices with real market option prices.
"""

import pandas as pd
from data_fetcher import get_stock_parameters
from monte_carlo import price_option
from visualization import plot_validation_comparison


def main():
    """Run Person 3's validation analysis."""
    
    print("=" * 60)
    print("Person 3: Market Data Validation")
    print("=" * 60)
    
    # Step 1: Load market data
    print("\nStep 1: Loading market option prices...")
    market_data = pd.read_csv('market_data.csv')
    print(market_data)
    
    # Step 2: Get stock parameters (same as Person 2)
    print("\nStep 2: Fetching AAPL parameters...")
    stock_params = get_stock_parameters('AAPL')
    S0 = stock_params['current_price']
    sigma = stock_params['volatility']
    
    T = 0.25    # 3 months
    r = 0.045   # Risk-free rate
    
    print(f"Current Price: ${S0:.2f}")
    print(f"Volatility: {sigma:.3f}")
    
    # Step 3: Calculate Monte Carlo prices for each strike
    print("\nStep 3: Calculating Monte Carlo prices for each strike...")
    mc_prices = []
    
    for strike in market_data['Strike']:
        price, _, _ = price_option(S0, strike, T, r, sigma, num_sims=50000)
        mc_prices.append(price)
        print(f"Strike ${strike:.2f}: MC Price = ${price:.2f}")
    
    # Step 4: Create validation table
    print("\nStep 4: Creating validation comparison...")
    validation = market_data.copy()
    validation['MC_Price'] = mc_prices
    validation['Error_Percent'] = ((validation['MC_Price'] - validation['Market_Price']) / 
                                    validation['Market_Price'] * 100)
    
    print("\n" + "=" * 60)
    print("Validation Results:")
    print("=" * 60)
    print(validation.to_string(index=False))
    
    # Step 5: Calculate summary statistics
    print("\n" + "=" * 60)
    print("Summary Statistics:")
    print("=" * 60)
    avg_error = validation['Error_Percent'].abs().mean()
    print(f"Average Absolute Error: {avg_error:.1f}%")
    print(f"Min Error: {validation['Error_Percent'].min():.1f}%")
    print(f"Max Error: {validation['Error_Percent'].max():.1f}%")
    
    # Step 6: Generate visualization
    print("\nStep 5: Generating validation plot...")
    plot_validation_comparison(
        validation['Strike'].tolist(),
        validation['MC_Price'].tolist(),
        validation['Market_Price'].tolist(),
        'person3_validation.png'
    )
    print("Created: person3_validation.png")
    
    # Step 7: Save results
    validation.to_csv('person3_validation_results.csv', index=False)
    print("Saved: person3_validation_results.csv")
    
    print("\n" + "=" * 60)
    print("Person 3 work completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
