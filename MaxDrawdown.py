# Worst possible return you could have seen if you bought at the high and sold at the low
# Calmar ratio is the ratio of annualised return over trailing 3 years,divided by the max drawdown over same period

import pandas as pd
import matplotlib.pyplot as plt

me_m = pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv', header=0, index_col=0, parse_dates=True, na_values=-99.99)

rets = me_m[['Lo 10', 'Hi 10']]
rets.columns = ['SmallCap', 'LargeCap']
print(rets.index)  # should be date
rets.index = pd.to_datetime(rets.index, format="%Y%m")
rets.index = rets.index.to_period('M')  # converts from 1st month to just month
print(rets.head())
rets = rets / 100
rets.plot.line()
print(rets.loc["1975"])
