import time

startTime = time.time()

year = 1901
daysTot = 0
sundays = 0

monthList = [31,28,31,30,31,30,31,31,30,31,30,31]

while year<2001:
    if year%4==0:
        monthList[1] = 29
    else:
        monthList[1] = 28
    for month in monthList:
        for i in range(1,month+1):
            daysTot += 1
            if (daysTot+6)%7==0 and i==1:
                sundays += 1
    year += 1
            
print(sundays)

endTime = time.time()

print(endTime-startTime)
