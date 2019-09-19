import csv

rows = []
matrix = [[-1]*14]*14
with open('sample.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader: 
        rows.append(row)
        
def getWeightMatrix(day, time):
    i = 1
    while(rows[i][5] != day):
        i+=261
    while(int(rows[i][6]) != time):
        i+=20
    for row in rows[i:i+21]:
        print(row)
        startNode = int(row[1])
        endNode = int(row[2])
        weight = float(row[7])
        matrix[startNode][endNode] = weight
    print("Matrix:")
    for r in matrix:
        print(r)
    
getWeightMatrix('Monday', 4)
  