# Understanding Your Monte Carlo Results

This guide explains how to interpret every part of the Monte Carlo simulation output.

---

## Part 1: Basic Parameters

When you run the code, you first see:

```
Stock: AAPL
Current Price (S0): $273.51
Strike Price (K): $274.00
Time to Maturity (T): 0.25 years (3 months)
Risk-free Rate (r): 0.045 (4.5%)
Volatility (σ): 0.283 (28.3%)
Number of Simulations: 50,000
```

### What do these mean?

**S0 = $273.51 (Current Stock Price)**
- The current price of AAPL stock
- This is our starting point for all simulations

**K = $274.00 (Strike Price)**
- The price specified in the option contract
- You have the right to buy the stock at this price
- Since K is approximately equal to S0, this is called an "at-the-money" option (no win, no lose)

**T = 0.25 years (3 months)**
- Time until the option expires
- After 3 months, you must decide whether to exercise the option

**r = 0.045 (4.5%)**
- Risk-free interest rate, typically the US Treasury yield
- Used to discount future cash flows to present value

**σ = 0.283 (28.3% Volatility)**
- The most important parameter
- Measures how much the stock price fluctuates
- 28.3% means AAPL has relatively high price volatility
- Higher volatility makes options more valuable because there's a greater chance of large price movements

---

## Part 2: Core Result

```
European Call Option Price: $18.82
```

### What this number means:

**$18.82 is the "fair price" for this option**

**In plain terms:**
- If you pay $18.82 today for this option
- In 3 months, you have the right to buy AAPL at $274
- If AAPL rises to $300 after 3 months:
  - Exercise option to buy at $274
  - Immediately sell at $300
  - Gross profit: $26
  - Minus option cost: $18.82
  - Net profit: $7.18

**If AAPL falls to $250 after 3 months:**
- You won't exercise the option (no point buying at $274 when market price is $250)
- The option expires worthless
- Loss: $18.82 (the option premium you paid)

### Why $18.82?

The Monte Carlo simulation ran 50,000 different scenarios:
- Some scenarios: AAPL rises significantly and you profit
- Some scenarios: AAPL falls and you lose the premium
- Average across all scenarios: $18.82 is the fair price

---

## Part 3: Simulation Statistics

```
Simulation Statistics:
  Average Final Stock Price: $276.59
  Std Dev of Final Prices: $39.30
  Probability of Finishing In-The-Money: 49.1%
```

### Breaking down each statistic:

#### Average Final Stock Price: $276.59

**Meaning:** Across 50,000 simulations, the average final stock price

**Interpretation:**
- Starting price: $273.51
- Average final price: $276.59
- Average increase: $3.08

**Why does it increase?**
- Because r = 4.5% is positive
- With a positive risk-free rate, stocks are expected to drift upward
- This follows financial theory (risk-neutral pricing)

#### Std Dev of Final Prices: $39.30

**Meaning:** Standard deviation of final stock prices

**Interpretation:**
- $39.30 relative to $273.51 is quite large
- This means the range of possible final prices is wide
- Approximately 68% of outcomes fall within:
  - $276.59 - $39.30 = $237.29
  - $276.59 + $39.30 = $315.89

**Why this matters:**
- Large volatility creates option value
- More price movement means higher chance of profitable outcomes

#### Probability of Finishing In-The-Money: 49.1%

**Meaning:** Probability that the option will be profitable to exercise

**What is "In-The-Money"?**
- For a call option: final stock price exceeds strike price
- Here: S_final is greater than $274

**Interpretation:**
- 49.1% of scenarios: AAPL ends above $274
- 50.9% of scenarios: AAPL ends at or below $274
- Roughly 50-50 odds

**Why not exactly 50%?**
- Because average final price ($276.59) is slightly greater than strike ($274)
- But it's very close, so probability is nearly even

---

## Part 4: Convergence Analysis

```
Convergence Analysis:
--------------------------------------------------
Simulations:    100 | Option Price: $20.48
Simulations:    500 | Option Price: $18.21
Simulations:   1000 | Option Price: $18.74
Simulations:   2000 | Option Price: $19.45
Simulations:   5000 | Option Price: $18.87
Simulations:  10000 | Option Price: $19.13
Simulations:  20000 | Option Price: $18.95
Simulations:  50000 | Option Price: $18.86
```

### What this table shows:

**Observing the price changes:**
- 100 simulations: $20.48 (unstable)
- 500 simulations: $18.21 (still fluctuating)
- 1000 simulations: $18.74
- ...
- 50,000 simulations: $18.86 (stable)

### Key insight:

**The Law of Large Numbers in action:**
- Few simulations produce unstable results
- More simulations produce increasingly stable results
- 50,000 is sufficient for reliable pricing

**Looking at the Convergence Plot:**
- X-axis: Number of simulations
- Y-axis: Calculated option price
- Red dashed line: Final stable price ($18.82)
- Blue curve: How price converges as simulations increase

**What you see in the plot:**
- Initially very unstable (curve bounces up and down)
- Gradually approaches the red line
- Eventually stabilizes around $18.82 - $18.86

---

## Part 5: Interpreting the Three Figures

### Figure 1: Stock Price Distribution

**What this shows:** The distribution of 50,000 possible final stock prices

#### Elements on the plot:

**Blue histogram:**
- X-axis: Final stock price (dollars)
- Y-axis: Probability density
- Shape: Bell curve (normal distribution)

**Three vertical lines:**
1. Green dashed line: Current Price = $273.51
   - Today's price
   
2. Red dashed line: Strike Price = $274.00
   - The exercise price
   - Critical line: outcomes to the right are profitable
   
3. Orange dashed line: Mean Final Price = $276.59
   - Average final price across simulations
   - Slightly to the right, indicating positive drift

#### How to interpret:

**Center of distribution:**
- Most probability concentrated between $200 and $350
- Center around $276
- Slightly right-skewed (positive drift)

**Position of red line:**
- Strike line is nearly at the center
- Area to the left (less than $274): approximately 50.9%
- Area to the right (greater than $274): approximately 49.1%
- This explains why In-The-Money probability is 49.1%

**Tails of distribution:**
- Right tail (extending right) is longer than left tail
- Small probability of very high stock prices
- This "positive surprise" possibility adds option value

**Key insight:**
```
Area to right of Strike = probability of profit
Further to the right = larger profits
```

---

### Figure 2: Convergence Plot

**What this shows:** How the price estimate stabilizes as simulations increase

#### Elements on the plot:

**X-axis:** Number of simulations (logarithmic scale)
- 100, 1000, 10000...

**Y-axis:** Calculated option price (dollars)

**Blue curve:** Each point shows the price calculated with that many simulations

**Red dashed line:** Final stable price of $18.82

#### How to interpret:

**Observe the curve shape:**
- Beginning: large fluctuations
  - 100 simulations: $20.48
  - 500 simulations: $18.21
  - Difference of $2.27
  
- Middle: convergence begins
  - 1000-5000 simulations: between $18.74 and $19.45
  
- End: very stable
  - 20,000 simulations: $18.95
  - 50,000 simulations: $18.86
  - Difference of only $0.09

**Key insight:**
```
More simulations = more accurate estimate
But also slower (more computation required)
50,000 is a good balance point
```

**What this proves:**
- The Monte Carlo method works
- Our result is reliable
- Additional simulations wouldn't change the price much

---

### Figure 3: Payoff Distribution

**What this shows:** Distribution of option payoffs at expiration

#### Elements on the plot:

**Pink histogram:**
- X-axis: Option payoff (dollars)
- Y-axis: Frequency (number of simulations)
- Very asymmetric shape

**Red dashed line:** Average Payoff = $19.04

**Yellow text box:** "50.9% of options expire worthless"

#### How to interpret:

**Large bar at left (X=0):**
- This is the tallest bar
- Approximately 25,450 occurrences (50.9% of simulations)
- Meaning: 50.9% of the time, the option expires worthless
- These are scenarios where stock price ends below $274

**Why do 50.9% of options expire worthless?**
- In 50.9% of scenarios, S_final is less than or equal to K
- You wouldn't exercise the option (buying at $274 when market price is lower)
- Payoff = 0

**Distribution to the right (X greater than 0):**
- These are profitable scenarios
- Extends from $0 to $300+
- Further right = fewer occurrences (high payoffs are rare)

**Average Payoff = $19.04:**
- This is the option's average value at expiration
- Note: slightly higher than option price ($18.82)
- Why? Because this hasn't been discounted to present value yet

**Key calculation:**
```
Option Price = Average Payoff × e^(-rT)
$18.82 ≈ $19.04 × e^(-0.045×0.25)
$18.82 ≈ $19.04 × 0.9888
$18.82 ≈ $18.83 ✓ This matches
```

**Key insight:**
```
Options have asymmetric payoffs:
- Limited downside (can only lose the premium)
- Unlimited upside (stock can rise indefinitely)

This asymmetry is why options have value
```

---

## Part 6: Deeper Understanding

### Why is Option Price ($18.82) less than Average Payoff ($19.04)?

**Answer: Time Value of Money**

$18.82 today equals $19.04 in 3 months

Calculation:
```
Present Value = Future Value × e^(-rT)
$18.82 = $19.04 × e^(-0.045 × 0.25)
$18.82 = $19.04 × 0.9888
$18.83 ≈ $18.82 ✓
```

### Why does average stock price increase?

**Risk-Neutral Pricing**

In Monte Carlo simulation, we assume:
```
Expected Return = Risk-free Rate = 4.5%
```

Therefore:
```
E[S_T] = S_0 × e^(rT)
E[S_T] = $273.51 × e^(0.045 × 0.25)
E[S_T] = $273.51 × 1.0113
E[S_T] = $276.60
```

This perfectly matches our result of $276.59

### The role of Volatility

**What does σ = 28.3% mean?**

Annualized standard deviation:
```
If AAPL is $273.51 today
In one year, there's a 68% probability it will be between:
  $273.51 × e^(-0.283) to $273.51 × e^(0.283)
  = $205 to $364
```

**Impact on option value:**
- Higher volatility makes options more valuable
- Why? Greater potential for large upward moves
- Remember: options have limited downside (only the premium)
- But unlimited upside potential

---

## Part 7: Practical Applications

### How to use these results?

#### Scenario 1: You want to buy this option

Compare market price vs Monte Carlo price:
- If market price is less than $18.82: Buy (undervalued)
- If market price is greater than $18.82: Don't buy (overvalued)
- If market price is approximately $18.82: Fair price

#### Scenario 2: Assess the risk

From Payoff Distribution:
- 50.9% probability of losing $18.82 (the premium)
- 49.1% probability of profit
- But when profitable, how much do you make on average?

Calculate:
```
Average profit when ITM = 
  Total Average Payoff / Probability of Profit
  = $19.04 / 0.491
  = $38.78
```

So:
- 50.9% of the time: lose $18.82
- 49.1% of the time: average gain of $38.78 - $18.82 = $19.96

**Expected Value:**
```
EV = 0.509 × (-$18.82) + 0.491 × ($19.96)
EV = -$9.58 + $9.80
EV ≈ $0.22
```

Close to zero, indicating fair pricing.

---

## Part 8: Summary - How to Explain to Others

### 30-second version:

"I used Monte Carlo methods to simulate 50,000 possible AAPL price paths. The results show that the fair price for this 3-month call option is $18.82. There's a 49.1% probability it will be profitable, with a 50.9% chance of losing the entire premium."

### 2-minute version:

"I implemented Monte Carlo option pricing:

**Method:**
- Simulated 50,000 possible AAPL price paths over 3 months
- Used the Geometric Brownian Motion model
- Calculated option payoff for each path
- Averaged and discounted to get the fair price

**Results:**
- Option price: $18.82
- Probability of profit: 49.1%
- Average final stock price: $276.59

**Verification:**
- Convergence plot shows 50,000 simulations provide stable results
- Results align with financial theory (risk-neutral pricing)
- Can be verified against the Black-Scholes formula"

### Presentation version (for class):

**Show the three figures and explain each:**

1. **Stock Price Distribution:**
   "This shows 50,000 possible final stock prices. The distribution is roughly normal, centered around $276. The strike price at $274 is near the center, indicating this is an at-the-money option."

2. **Convergence Plot:**
   "This demonstrates the validity of the Monte Carlo method. As simulation count increases, the price moves from unstable to converging toward $18.82. 50,000 simulations provide sufficient accuracy."

3. **Payoff Distribution:**
   "This illustrates the asymmetric nature of option payoffs. 50.9% of options expire worthless (the large bar on the left), but when profitable, gains can be substantial (the right tail). This asymmetry is the source of option value."

---

## Understanding the Key Numbers

### Important relationships:

1. **In-The-Money probability (49.1%) is not the same as profit probability**
   - Some ITM outcomes only generate small profits
   - Others generate large profits

2. **Why the distribution isn't perfectly normal:**
   - Stock prices follow a log-normal distribution
   - Cannot be negative
   - Results in a longer right tail

3. **Present value vs Future value:**
   - Option price ($18.82) is present value
   - Average payoff ($19.04) is future value
   - Difference reflects time value of money

### Critical formulas used:

**Geometric Brownian Motion:**
```
S_T = S_0 × exp((r - 0.5σ²)T + σ√T·Z)
```
Where Z is a random normal variable

**Present Value:**
```
PV = FV × e^(-rT)
```

**Option Payoff (Call):**
```
Payoff = max(S_T - K, 0)
```

---

The key takeaway is that Monte Carlo pricing works by averaging outcomes across many possible future scenarios, weighted by their probabilities and discounted to present value.
