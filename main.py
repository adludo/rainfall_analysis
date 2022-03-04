from functions import *
import numpy as np


header, rows = RawData()
# LPrint(rows, 0, 10)

rain_tomorrow = [el[0] for el in rows]
location = LocationData(rows)

rain_tomorrow_arr = np.array(rain_tomorrow)
location_arr = np.array(location)

unq_locations = np.unique(location_arr)

this_city = CityData('Darwin', rows)

print(this_city)


# yes_num = np.count_nonzero(rain_tomorrow_arr == 'Yes') 

# print (len(unq_locations))

