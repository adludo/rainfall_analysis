from functions import *
import numpy as np


header, rows = RawData()

# LPrint(rows, 0, 10)
# print (rows[1][0])

rain_tomorrow = [el[0] for el in rows]
print (rain_tomorrow)
# arr = np.array([])
# new_arr = np.append(arr, 10)

# print('New Array: ', new_arr)

# data_len = len(rows)
# cnt = 0
# for i in range(data_len):
#     # print(rows[i][0])
#     if rows[i][0] == 'No':
#         # print('test')
#         cnt = cnt + 1 

# print(cnt)
