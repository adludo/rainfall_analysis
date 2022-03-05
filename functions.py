import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plot the distribution by whether it rains tomorrow
def PlotByRainTomorrow (df, field):
    # ax = df.hist(column = 'humidity_3pm', bins=12, alpha=0.5)
    ax = df.hist(column = field, \
        by='rain_tomorrow', \
        figsize=(5, 4) \
    )
    plt.show()

# Create binned dataframe pivot table for whether it rains or not
def BinnedRainCond (df, field, bins):
    df, bin_name = BinnedDataField (df, field, bins) 
    df['count'] = 1
    result = df.pivot_table(
        index=[bin_name], columns='rain_tomorrow', values='count',
        fill_value=0, aggfunc=np.sum
    )
    return result

# Include binned field in dataframe 
# Q1b
def BinnedDataField (df, field, bins):
    bin_range = FRange(bins)
    bn = field + '_binned'
    df[bn] = pd.qcut(df[field], \
        q=bin_range, \
        # labels=['A', 'B', 'C', 'D', 'E'] \
    )
    # print(df)
    return df, bn

# Create a floating range for bins in the dataframe
def FRange(n):
    test_range = range(n)
    quotients = [number / len(test_range) for number in test_range]
    quotients.append(1)
    return quotients

# Answer Q1a with pandas
def Question1av2():
    data = pd.read_csv("rainfall_prediction_data.csv")
    print(data.rain_tomorrow.value_counts().reset_index(name='Counts'))
    return

# Answer Q1a no pandas
def Question1a():
    header, rows = RawData()
    rain_tom = [el[0] for el in rows]
    rain_tom_arr = np.array(rain_tom)
    yes_num = np.count_nonzero(rain_tom_arr == 'Yes') 
    print (yes_num)
    return yes_num

# Get the data under a certain header with 'NA's and as floats
def CleanedHeaderDataF(hdr, rs): # header, row data
    clnhdrdat = HeaderData(hdr, rs)
    new_arr = np.delete(clnhdrdat, np.where(clnhdrdat == 'NA'))
    new_arr_f = new_arr.astype(np.float)
    return new_arr_f

# Get the data under a certain header
def HeaderData(hdr, rs): # header, row data
    if hdr == 'rain_tomorrow':
        col = 0
    elif hdr == 'date':
            col = 1
    elif hdr == 'location':
            col = 2
    elif hdr == 'min_temp':
            col = 3
    elif hdr == 'rainfall':
            col = 4
    elif hdr == 'evaporation':
            col = 5
    elif hdr == 'sunshine':
            col = 6
    elif hdr == 'humidity_3pm':
            col = 7
    elif hdr == 'pressure_3pm':
            col = 8
    sub_data = []
    for r in rs:
        # print (r)
        # if r[col] == hdr:
        sub_data.append(r[col])
    sub_data_arr = np.array(sub_data)
    return sub_data_arr


# Get data for a certain city
def CityData(city, rs):
    sub_data = []
    for r in rs:
        if r[2] == city:
            sub_data.append(r)
    return sub_data

# Get all locations, can later use to get unique locations
def LocationData(rs):
    location = [el[2] for el in rs]
    return location

# Import csv data and separate into header and rows
def RawData():
    rs = []
    with open('rainfall_prediction_data.csv') as file:
        csvreader = csv.reader(file)
        hdr = next(csvreader)
        for r in csvreader:
            rs.append(r)    
    return hdr, rs

# Print a limited amount of data
def LPrint(arr,l_start,l_end): #array data, line start, line end
    for i in range(l_start,l_end):
        print(arr[i])