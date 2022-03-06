from functions import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

# Code starts here
source = pd.read_csv("rainfall_prediction_data.csv")
q = 10 # number of bins - 1

# Question1a()
# Question1av2()

pw_table = CalculatingWoe(source, 'humidity_3pm', q)
print (pw_table)
iv_final = pw_table['iv_nosum'].sum()
print(iv_final)

# PlotByRainTomorrow (source, 'pressure_3pm')

# print(result.iloc[0])
