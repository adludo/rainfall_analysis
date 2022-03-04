import csv

rows = []

with open('rainfall_prediction_data.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)    
# file = open('rainfall_prediction_data.csv')
# type(file)

# print (csvreader)

print(header)
print(rows)