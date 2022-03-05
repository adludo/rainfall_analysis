from functions import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

source = pd.read_csv("rainfall_prediction_data.csv")

# Question1a()
# Question1av2()

# Different selection fields 
# rain_tomorrow        
# date      
# location  
# min_temp  
# rainfall  
# evaporation  
# sunshine  
# humidity_3pm  
# pressure_3pm 
# humidity_3pm_binned

# result, bins = BinnedDataField(source, 'humidity_3pm', 7)
p_table = BinnedRainCond(source, 'humidity_3pm', 7)

print(p_table.iloc[1].Yes)

# print(result['humidity_3pm_binned'].value_counts())
# result = BinnedDataField(source, 'humidity_3pm', 7)
# PlotByRainTomorrow (source, 'evaporation')

# print(result.iloc[0])
