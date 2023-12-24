from time import time

startTime = time()

tempList1 = []
tempList2 = []
fullList = []
fullListStr = []
num = 1

while num<10000:
    half = int(num/2)
    tempList1.append(1)
    for i in range (2, half+1):
        if num%i==0:
            tempList1.append(i)
    tempSum1 = sum(tempList1)
    half = int(tempSum1/2)
    tempList2.append(1)
    for j in range(2, half+1):
        if tempSum1%j==0:
            tempList2.append(j)
    tempSum2 = sum(tempList2)
    if num==tempSum2 and num!=tempSum1:
        fullList.append(num)

    num += 1
    tempList1 = []
    tempList2 = []
    
for a in fullList:
    fullListStr.append(str(a))
    
fullStr = ", ".join(fullListStr)

print("The amicable numbers below 10,000 are -> " + fullStr + "\n")
print("Therefore, the sum of the amicable numbers below 10,000 is -> " + str(sum(fullList)))

endTime = time()
runningTime = endTime-startTime

print("\nIt took: ", runningTime, "seconds")
