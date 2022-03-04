import csv

# Import csv data and separate into header and rows
def raw_data():
    rs = []

    with open('rainfall_prediction_data.csv') as file:
        csvreader = csv.reader(file)
        hdr = next(csvreader)
        for r in csvreader:
            rs.append(r)    
        
    # print(header)
    # print(rows)
    return hdr, rs
