import pandas as pd

prices = pd.DataFrame(

    {
        "Blue": [8.70, 8.91, 8.71, 8.43, 8.73],
        "Orange": [10.66, 11.08, 10.71, 11.59, 12.11]

    }

)
# iloc is index location

except_first = prices.iloc[1:]  # everything except 1st row

except_last = prices.iloc[:-1]  # everything except last row

division = except_first.values / except_last - 1  # needs .values due to index alignment

print(division)

better_return_method = prices / prices.shift(1) - 1

print(better_return_method)

percent_change = prices.pct_change()
print(percent_change)
