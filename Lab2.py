import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

prices = pd.read_csv('sample_prices.csv')
returns = prices.pct_change()
returns = returns.dropna()
print(returns.std())

deviations = returns - returns.mean()
squared_deviations = deviations ** 2
variance = squared_deviations.sum() / (returns.shape[0] - 1)
volatility = np.sqrt(variance)

# annualise Vol

volatility = volatility * np.sqrt(12)
print(volatility)
