#! /opt/homebrew/bin/python3

########################################

from time import time
from math import sqrt

########################################

startTime = time()

ans = 0

for num in range(2, 10_001):

    if sqrt(num)%1!=0:

        tempList = []

        rootOfNum = sqrt(num)
        leadingDigit = int(rootOfNum)

        fraction = 1/(rootOfNum-leadingDigit)

        for i in range(10):
            leadingDigitOfFrac = int(fraction)
            tempList.append(leadingDigitOfFrac)
            fraction -= leadingDigitOfFrac
            fraction = fraction**(-1)

        five1 = tempList[0:5]
        five2 = tempList[5:10]
        three1 = tempList[0:3]
        three2 = tempList[3:6]
        three3 = tempList[6:9]
        one1 = tempList[0]
        one2 = tempList[1]
        one3 = tempList[2]
        one4 = tempList[3]
        one5 = tempList[4]
        one6 = tempList[5]
        one7 = tempList[6]
        one8 = tempList[7]
        one9 = tempList[8]
        one10 = tempList[9]

        if five1 == five2:
            ans += 1
        elif three1 == three2 and three2 == three3:
            ans +=1
        elif one1 == one2 and one2 == one3 and one3 == one4 and one4 == one5 and one5 == one6 and one6 == one7 and one7 == one8 and one8 == one9 and one9 == one10:
            ans += 1

print(ans)

finishTime = time()

########################################

print(f"The code took: {finishTime-startTime} seconds, to run!")
