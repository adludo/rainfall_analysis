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
q = 5 # number of bins

# Question1a()
# Question1av2()

pw_table = CalculatingWoe(source, 'rainfall', q)

# PlotByRainTomorrow (source, 'pressure_3pm')

# print(result.iloc[0])
