from functions import *
import numpy as np


header, rows = RawData()
# LPrint(rows, 0, 10)

rain_tomorrow = [el[0] for el in rows]

rain_tomorrow_arr = np.array(rain_tomorrow)
yes_num = np.count_nonzero(rain_tomorrow_arr == 'Yes') 

print (yes_num)

