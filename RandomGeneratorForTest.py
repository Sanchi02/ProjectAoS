import csv
import pandas as pd
from random import random,seed, randrange
from math import ceil

def getPacketsFlowing(day,time,bandwidth):
    workingDays = ["Monday","Tuesday","Wednesday","Thrusday","Friday"]
    workingHours = [10,12,14,16,18]
    if((day in workingDays) and (time in workingHours)):
        return randrange(ceil(0.7*bandwidth), bandwidth)
    if((day in workingDays) and (time not in workingHours)):
        return randrange(ceil(0.5*bandwidth), ceil(0.8*bandwidth))
    if((day not in workingDays) and (time in workingHours)):
        return randrange(ceil(0.3*bandwidth), ceil(0.6*bandwidth))
    if((day not in workingDays) and (time not in workingHours)): 
        return randrange(ceil(0.1*bandwidth), ceil(0.4*bandwidth))   
    return 50

# row = [EP1, Ep2, PacketsFlowing, Bandwidth, Dow, TOD]
dicty = {0:[1,2,3], 1:[2,7], 2:[5], 3:[4,10], 4:[5,6], 5:[8,12], 6:[7], 7:[9], 8:[9], 9:[11,13], 10:[11,13], 11:[12]}
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday","Friday", "Saturday"]
seed(5)
allRows = []
for _ in range(5):
    allRows = []
    tmpID = 0
    for day in weekdays:
        for i in range(0,26,2):
            for val in dicty:
                for node in dicty[val]:
                    bandwidth = randrange(5,15)*10
                    packet = getPacketsFlowing(day,i,bandwidth)
                    allRows.append([tmpID,val,node,bandwidth, packet, day, i])
                    tmpID += 1
    df = pd.DataFrame(allRows,columns=['ID','EP1','EP2', 'Bandwidth', 'PacketsFlowing(1Kb)','DayOfTheWeek', 'TimeHour'])
    stringy = "TestSnapshotForWeek"+str(_)+".csv"
    df.to_csv(stringy, index=False)
        


print(df)



