Monte Carlo Option Pricing Project
===================================

Project Overview
----------------
This project implements Monte Carlo simulation for pricing European call options
on Apple (AAPL) stock. The work is divided among four team members, with each
person responsible for specific components.

Team Structure
--------------
- Person 1: Introduction, theory, and poster design
- Person 2: Core Monte Carlo implementation with real data
- Person 3: Market data collection and validation
- Person 4: Parameter sensitivity analysis

Installation
------------
1. Install Python 3.8 or higher
2. Install required packages:
   
   pip install -r requirements.txt

Project Files
-------------
Core Modules:
- data_fetcher.py - Functions for fetching stock data and calculating volatility
- monte_carlo.py - Core Monte Carlo simulation functions
- visualization.py - Plotting and charting functions

Person-Specific Scripts:
- person2_montecarlo.py - Person 2's main implementation script
- person3_validation.py - Person 3's validation analysis
- person4_sensitivity.py - Person 4's sensitivity analysis

Data Files:
- market_data.csv - Real market option prices collected by Person 3

How to Run
----------
Person 2 (Core Implementation):
   python person2_montecarlo.py

Person 3 (Validation):
   python person3_validation.py

Person 4 (Sensitivity Analysis):
   python person4_sensitivity.py

What Each Person Does
----------------------

Person 2: Core Implementation
- Fetches real AAPL stock data using Yahoo Finance
- Calculates historical volatility from 1 year of price data
- Runs 50,000 Monte Carlo simulations to price options
- Generates three visualizations:
  * Stock price distribution histogram
  * Convergence analysis plot
  * Option payoff distribution

Output Files:
- person2_stock_distribution.png
- person2_convergence.png
- person2_payoff_distribution.png

Person 3: Validation
- Uses real market option prices from Yahoo Finance
- Compares Monte Carlo prices to actual market prices
- Calculates validation error percentages
- Creates comparison visualization

Input Required:
- market_data.csv (three strikes with market prices)

Output Files:
- person3_validation.png
- person3_validation_results.csv

Person 4: Sensitivity Analysis
- Tests how volatility affects option prices
- Tests how strike price affects option prices
- Generates two sensitivity plots
- Summarizes key findings

Output Files:
- person4_volatility_sensitivity.png
- person4_strike_sensitivity.png

Key Parameters Used
-------------------
Stock: AAPL (Apple Inc.)
Current Price (S0): Fetched from Yahoo Finance
Strike Price (K): $274.00 (at-the-money)
Time to Maturity (T): 0.25 years (3 months)
Risk-free Rate (r): 0.045 (4.5%)
Volatility (σ): Calculated from historical data (~0.28)
Number of Simulations: 50,000

Understanding the Results
--------------------------
The Monte Carlo method works by:
1. Simulating 50,000 possible future stock prices
2. Calculating the option payoff for each simulated price
3. Averaging the payoffs and discounting to present value

Expected Results:
- Option price around $18-19 for K=$274
- Validation error typically 10-20% (acceptable for academic projects)
- Higher volatility leads to higher option prices
- Lower strike prices lead to higher call option prices

There could be errors!!
----------------------
Our simplified model assumes:
- No dividends
- Constant volatility
- European-style options (exercise only at expiration)

Real market prices include:
- Dividend expectations
- Changing volatility over time
- American-style exercise options
- Market supply and demand effects
