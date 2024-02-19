#! /opt/homebrew/bin/python3

########################################

from time import time
from mpmath import mp

########################################

startTime = time()

mp.dps = 400

ans = 0

for num in range(2, 10_001):

    if mp.sqrt(num)%1!=0:

        tempList = []

        rootOfNum = mp.sqrt(num)
        leadingDigit = int(rootOfNum)

        fraction = 1/(rootOfNum-leadingDigit)

        for i in range(300):
            leadingDigitOfFrac = int(fraction)
            tempList.append(leadingDigitOfFrac)
            fraction -= leadingDigitOfFrac
            fraction = mp.power(fraction, (-1))

        if len(tempList)%2 != 0:
            tempList = tempList[0:-1]

        while len(tempList)%2 == 0 and tempList[0:len(tempList)//2] != tempList[len(tempList)//2:len(tempList)]:
            tempList = tempList[0:-2]

        if len(tempList) != 0:

            while len(tempList)%2 == 0 and tempList[0:len(tempList)//2] == tempList[len(tempList)//2:len(tempList)]:
                tempList = tempList[0:len(tempList)//2]

            if len(tempList)%2 != 0:
                ans += 1
        
print(ans)

finishTime = time()

########################################

print(f"The code took: {finishTime-startTime} seconds, to run!")
