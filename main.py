from functions import *
import numpy as np
import matplotlib.pyplot as plt

header, rows = RawData()
# ## Question 1a
# answer1 = Question1(rows)
# print (answer1)

humidity_data = CleanedHeaderDataF('humidity_3pm', rows)

data_min = np.amin(humidity_data)
data_max = np.amax(humidity_data)
# print(data_max)

plt.hist(humidity_data, bins = 50)



plt.show()

