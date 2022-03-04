import csv

# Import csv data and separate into header and rows
def raw_data():
    rs = []
    with open('rainfall_prediction_data.csv') as file:
        csvreader = csv.reader(file)
        hdr = next(csvreader)
        for r in csvreader:
            rs.append(r)    
    return hdr, rs

# Print a limited amount of data
def lprint(arr,l_start,l_end): #array data, line start, line end
    for i in range(l_start,l_end):
        print(arr[i])