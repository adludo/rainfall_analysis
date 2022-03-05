from functions import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# header, rows = RawData()
# ## Question 1a
# answer1 = Question1(rows)
# print (answer1)

source = pd.read_csv("rainfall_prediction_data.csv")

## Question 1a v2
# print(df.rain_tomorrow.value_counts().reset_index(name='Counts'))



# test_range = range(7)
# quotients = [number / len(test_range) for number in test_range]
# quotients.append(1)


# df['humidity_bin'] = pd.qcut(df['humidity_3pm'], \
#     q=quotients, \
#     # labels=['A', 'B', 'C', 'D', 'E'] \
#     )

# df['count'] = 1

# result = df.pivot_table(
#     index=['humidity_bin'], columns='rain_tomorrow', values='count',
#     fill_value=0, aggfunc=np.sum
# )
result = BinnedRainCond(source, 'humidity_3pm', 7)
print(result)
# print(result.iloc[0])







# print(df['humidity_bin'].value_counts())
# ax = df.hist(column = 'humidity_3pm', bins=12, alpha=0.5)
# plt.show()


# data_min = np.amin(humidity_data)
# data_max = np.amax(humidity_data)


# ## Plotting
# plt.hist(humidity_data, bins = 50)
# plt.show()

