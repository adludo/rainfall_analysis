import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Calculation of exp_w_i and IV
# Q1d & Q2
def CalculatingExpW(p_table, exp_w_arr, m, n, q):
    iv_array_nosum = []
    for i in range(q):
        # print(i)
        yes_val = p_table.iloc[i].Yes
        no_val = p_table.iloc[i].No

        n_val = yes_val + no_val
        m_val = yes_val

        frac1 = m_val/m
        frac2 = (n - m)/(n_val - m_val)
        # print(frac2)
        exp_w_val = frac1 * frac2
        # print('error?')
        exp_w_arr.append(exp_w_val)
        # print('error2?')

        # Calculate IV here?
        iv_val_nosum = (frac1 - (1/frac2)) * math.log(exp_w_val)
        iv_array_nosum.append(iv_val_nosum)

    return exp_w_arr, iv_array_nosum

# Add the Weight of Evidence and Information Value into the pivot table summarising the data
# Q1d & Q2
def CalculatingWoe (df, field, q):
    # Initiating variables
    exp_w_arr = []
    n_arr = []
    n = len(df.index)
    m_test = df.rain_tomorrow.value_counts().reset_index(name='Counts')
    m = m_test.iloc[1].Counts
    # print('test')
    p_table = BinnedRainCond(df, field, q) # pivot table
    # print('test2')

    # Calculating the exponential weight of evidence to then take log
    exp_w_arr, iv_array_nosum = CalculatingExpW(p_table, exp_w_arr, m, n, q)

    p_table['exp_w'] = exp_w_arr
    p_table['iv_nosum'] = iv_array_nosum

    exp_w_col = p_table.columns.get_loc('exp_w')
    w_arr = np.log(p_table.iloc[:,exp_w_col].values)
    # print (p_table.iloc[:,2].values)
    p_table['weight_of_evidence'] = w_arr
    # print(p_table)
    return p_table

# Plot the distribution by whether it rains tomorrow
def PlotByRainTomorrow (df, field):
    # ax = df.hist(column = 'humidity_3pm', bins=12, alpha=0.5)
    ax = df.hist(column = field, \
        by='rain_tomorrow', \
        figsize=(5, 4) \
    )
    plt.show()

# Create binned dataframe pivot table for whether it rains or not
# Q1c 
def BinnedRainCond (df, field, bins):
    # print('new_test')
    df, bn = BinnedDataField (df, field, bins) 
    # print('new_test2')
    df['count'] = 1
    result = df.pivot_table(
        index=[bn], columns='rain_tomorrow', values='count',
        fill_value=0, aggfunc=np.sum
    )
    # print(result)
    return result

# Using qcut to create bins
def BinQcut (df, field, bins):
    bn = field + '_binned'
    # print(df)
    bin_range = FRange(bins)
    df[bn] = pd.qcut(df[field], \
        q=bin_range, \
        # labels=['A', 'B', 'C', 'D', 'E'] \
        # duplicates= 'drop', \
    )
    return df, bn

# Using cut to create bins
def BinCut (df, field, bin_num):
    bn = field + '_binned'
    print (bin_num)
    df[bn] = pd.cut(df[field], \
        bin_num, \
        # labels=['A', 'B', 'C', 'D', 'E'] \
    )
    return df, bn

# Include binned field in dataframe 
# Q1b 
def BinnedDataField (df, field, bins):
    print ('bug_test')
    df, bn = BinQcut(df, field, bins) # BIN USING QCUT
    # df, bn = BinCut(df, field, bins) # BIN USING CUT
    # print ('bug_test2')
    return df, bn

# Create a floating range by % for bins in the dataframe
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