import csv

# Get data for a certain city
def CityData(city, rs):
    sub_data = []
    for r in rs:
        if r[2] == city:
            sub_data.append(r)
    return sub_data

# Get the unique locations
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