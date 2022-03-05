from functions import *
import numpy as np
import matplotlib.pyplot as plt

header, rows = RawData()
# ## Question 1a
# answer1 = Question1(rows)
# print (answer1)

humidity_data = HeaderData('humidity_3pm', rows)
print(humidity_data[:20])
new_arr = np.delete(humidity_data, np.where(humidity_data == 'NA'))
print(new_arr[:20])



new_arr_f = new_arr.astype(np.float)
print(new_arr_f[:20])

plt.hist(new_arr_f, bins = 50)

data_min = np.amin(new_arr_f)
data_max = np.amax(new_arr_f)
print(data_max)

plt.show()
# print(humidity_data[:10])
# print (header)
# print('Row data', rows[:10])


# HeaderData(hdr, rs)

# print (len(unq_locations))

