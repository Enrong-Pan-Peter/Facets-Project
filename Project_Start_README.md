# Monte Carlo Options Pricing - Project Plan

## 项目概述
我们要用Monte Carlo方法来给期权定价，并且用真实市场数据来验证我们的模型。我也不太了解金融的东西，所以才想选择这个题目。所以如果下面的terms有解释不清楚的，建议大家还是自己查一查。

---

## Phase 1: 前期准备 - 理解核心概念

在开始coding之前，大家需要先理解一些基本概念。建议每个人都花一点时间左右看一下这些内容。

### 需要了解的核心概念：

#### 1. **Options Pricing 相关**
- **Call Option (看涨期权)**: 在未来某个时间以特定价格买入股票的权利
- **Put Option (看跌期权)**: 在未来某个时间以特定价格卖出股票的权利
- **Strike Price (执行价格)**: 期权合约中约定的买卖价格
- **Expiration Date**: 期权到期日

#### 2. **Monte Carlo Method**
- 基本思想：通过大量随机模拟来估算期权的合理价格
- 为什么用这个方法：因为直接用公式计算很复杂，Monte Carlo用 brute force 方法模拟成千上万种可能的股价走势

#### 3. **Statistical/Financial 概念**
- **Volatility (波动率 σ)**: 股价变动的剧烈程度，波动越大，期权越值钱
- **Risk-free Rate (无风险利率 r)**: 通常用国债收益率，大概4-5%
- **Random Walk**: 股价的random walk模型，假设股价变动是随机，很难掌握规律的
- **Black-Scholes Equation**: 期权定价的经典公式，我们用它来验证Monte Carlo的结果

### 推荐options pricing入门
- YouTube："Monte Carlo Option Pricing Python" 或 "Options Pricing Explained"
- 推荐看10-15分钟的intro视频就够了，完全不需要深入理解数学推导，我们只需要能用

---

## Phase 2: 任务分工（每个人大概3小时吧）

### **Person 1: 文字内容 + Poster整合 （比较简单的）** 

**主要职责：**
1. 写poster的所有文字部分
2. 在Overleaf设置poster模板
3. 整合其他人的图和代码

**具体任务：**

#### 1.1 Introduction Section
写清楚以下内容：
- 什么是期权？用简单的例子解释
- 为什么期权定价很难？
- Monte Carlo method 是什么？为什么选它？

**参考框架 (from chatgpt)：**
```
什么是Option:
一个金融合约，给你在未来某个日期以特定价格（strike price）买或卖股票的权利（不是义务）。
核心问题是：今天这个合约值多少钱？

Monte Carlo的思路：
与其用复杂公式，不如"暴力破解"：
1. 模拟50,000种可能的股价走势
2. 对每种走势，计算期权的价值
3. 把50,000个价值平均一下
4. 这个平均值就是期权的合理价格
```

#### 1.2 Mathematical Foundation
解释核心数学公式：
- Geometric Brownian Motion (股价随机游走模型)
- Payoff function: max(S_T - K, 0) for call options
- 简单提一下Black-Scholes formula（用来验证的）

**Note:** 不需要推导，只需要写出公式并解释每个符号是什么意思。

#### 1.3 Overleaf Poster Setup
- 用提供的模板链接 (https://www.overleaf.com/gallery/tagged/poster)
- 参考LASSO和Sharygin两个例子的排版
- 留好位置给其他人的图和代码 （要是其他人的图太丑了，你放心要他们重做好看点的图）

**Poster结构建议 (from chatgpt)：**
```
Left Column:
- What is an Option?
- Why Monte Carlo?
- Mathematical Foundation

Middle Column:
- Implementation (代码snippet)
- Basic Results (histogram等)

Right Column:
- Validation (和市场价格对比)
- Parameter Sensitivity Analysis
- Key Findings

Bottom:
- References
```

#### 1.4 Final Integration 
- 收集Person 2, 3, 4的所有图片和代码
- 整合到poster里
- 确保格式统一，字体大小合适
- 写Results Summary和Conclusion
---

### **Person 2: Core Implementation（写代码 1）** 

**主要职责：**
1. 实现Monte Carlo核心算法
2. fetech真实股票数据
3. 计算 historical volatilities
4. 生成基础图表

**具体任务：**

#### 2.1 Setup Environment 
```bash 
pip install yfinance numpy pandas matplotlib scipy
```

#### 2.2 实现Monte Carlo Function
写一个函数 `monte_carlo_option()` 来计算期权价格。

**需要的inputs:**
- S0: 当前股价
- K: strike price
- T: 到期时间（年）
- r: 无风险利率
- sigma: 波动率
- num_sims: 模拟次数

**Output:**
- 期权价格

**核心逻辑：**
1. 生成50,000个随机数（代表未来股价的随机性）
2. 用Geometric Brownian Motion公式算出50,000个可能的最终股价
3. 对每个股价，计算期权payoff = max(S_T - K, 0)
4. 把50,000个payoff平均，再discount回现在的价值

#### 2.3 fetch real data
用yfinance抓取Apple (AAPL) 的历史数据：
- 过去一年的股价
- 计算历史波动率（用daily returns的标准差）
- 获取当前股价作为S0

#### 2.4 visualize
生成三个图：
1. **Histogram of Simulated Stock Prices**: 50,000个模拟出来的最终股价分布
2. **Convergence Plot**: 随着模拟次数增加，期权价格如何收敛
3. **Payoff Distribution**: 期权payoff的分布

保存为PNG文件，给Person 1放到poster里。

**Deliverables:**
- `monte_carlo.py` (核心代码文件)
- 3张图片 (PNG格式)

---

### **Person 3: Data Collection + Validation（写代码 2）** 

**主要职责：**
1. 收集真实的期权市场价格
2. 对比Monte Carlo价格和真实市场价格
3. 创建validation table和plot

**具体任务：**

#### 3.1 收集市场数据 

**Steps:**
1. 去 Yahoo Finance: https://finance.yahoo.com/quote/AAPL/options
2. 选一个expiration date（1-3个月后的）
3. 看Call Options那个表格
4. mark 4个不同strike的数据

**需要收集的信息：**
- Strike Price (比如185, 190, 195, 200)
- Last Price (市场上最后成交价)
- Expiration Date
- Type (都是Call)

**保存到CSV文件 `real_option_prices.csv`:**
```csv
Strike,Market_Price,Expiration,Type
185.00,15.20,2025-01-17,Call
190.00,12.45,2025-01-17,Call
195.00,9.80,2025-01-17,Call
200.00,7.50,2025-01-17,Call
```

#### 3.2 写Validation代码 
用Person 2写好的`monte_carlo_option()`函数，对每个strike price:
1. 用Monte Carlo算出理论价格
2. 和你收集的Market_Price对比
3. 计算误差百分比

**生成一个对比表格（大概这样的东西）：**
```
Strike | Market Price | MC Price | Error (%)
185    | 15.20        | 15.05    | 1.0%
190    | 12.45        | 12.38    | 0.6%
...
```

#### 3.3 visualize
- Bar chart对比：Monte Carlo vs Market Price
- 或者Scatter plot with line y=x (理想情况MC=Market)

**Deliverables:**
- `real_option_prices.csv`
- `validation.py` (validation代码)
- Validation table (可以是matplotlib table或者LaTeX table)
- 1-2张对比图
---

### **Person 4: Parameter Sensitivity Analysis（测试代码）** 

**主要职责：**
1. 研究不同参数如何影响期权价格
2. 生成多个可视化图表
3. 总结findings

**具体任务：**

#### 4.1 Volatility Analysis (1 hour)
测试不同的波动率对期权价格的影响。

**Steps:**
1. 用Person 2的`monte_carlo_option()`函数
2. 固定其他参数（S0=100, K=100, T=1, r=0.05）
3. 改变sigma: 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4
4. 记录每个sigma对应的期权价格

**生成Line Plot:**
- X轴: Volatility (σ)
- Y轴: Option Price
- 标题: "Effect of Volatility on Option Price"

**写2-3句话总结：** 比如"波动率越高，期权价格越高，因为..."

#### 4.2 Strike Price Analysis (1 hour)
测试不同的strike price对期权价格的影响。

**Steps:**
1. 固定S0=185 (当前AAPL股价), sigma=0.28, T=0.25, r=0.045
2. 改变K: 175, 180, 185, 190, 195, 200, 205
3. 记录每个K对应的期权价格

**生成Line Plot:**
- X轴: Strike Price (K)
- Y轴: Option Price
- 标题: "Option Price vs Strike Price"

**写2-3句话总结：** 比如"Strike越低，call option越值钱，因为..."

#### 4.3 2D Heatmap (optional,会比较好看，但要花多半小时吧)
同时改变volatility和strike，生成一个热力图。

**用seaborn创建heatmap:**
- X轴: Strike Price
- Y轴: Volatility
- 颜色: Option Price

这个图看起来会很professional！

**Deliverables:**
- `sensitivity_analysis.py`
- 2-3张分析图
- 简短的findings总结（3-5句话）

---

## 使用的标准参数

为了保持一致，大家都用这些参数：
```python
# Standard Parameters
S0 = 当前AAPL股价 (从yfinance获取)
K = 100 或 当前股价 (at-the-money)
T = 0.25  # 3个月 = 0.25年
r = 0.045  # 4.5% 无风险利率
sigma = 从历史数据计算出来的值 (大概0.25-0.30)
num_sims = 50000  # 模拟次数
```
---

## 有问题就问！

如果任何人在任何步骤卡住了，马上在group chat里说。有bug很正常，大家可以互相帮忙debug。and 如果你太忙了也要说，我们可以互相split work的。

Good luck! 💪