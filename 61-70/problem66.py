#! /opt/homebrew/bin/python3

########################################

from time import time
from mpmath import mp

########################################

startTime = time()

mp.dps = 1000

ans = [0, 0]

finalList = []

for D in range(2, 14):

    if mp.sqrt(D)%1!=0:
        print(D)

        tries = 0

        rootOfNum = mp.sqrt(D)
        leadingDigit = int(rootOfNum)

        fraction = 1/(rootOfNum-leadingDigit)

        while True:
            tempList = []

            tries += 1

            for i in range(tries):
                leadingDigitOfFrac = int(fraction)
                tempList.append(leadingDigitOfFrac)
                fraction -= leadingDigitOfFrac
                fraction = mp.power(fraction, (-1))

            ansList = [[1, tempList[-1]]]

            for i in range(len(tempList)-2, 0, -1):
                ansList.append([ansList[-1][1], tempList[i] * ansList[-1][1] + ansList[-1][0]])

#            print(ansList[-1][1] * leadingDigit + ansList[-1][0])

            if (ansList[-1][1] * leadingDigit + ansList[-1][0])**2 - D * (ansList[-1][1])**2 == 1:
                if (ansList[-1][1] * leadingDigit + ansList[-1][0]) > ans[0]:
                    ans = [ansList[-1][1] * leadingDigit + ansList[-1][0], (ansList[-1][1]), D]
                break

            if tries == 9:
                break

        print(tempList)
        print(ansList)

        
print(ans)

finishTime = time()

########################################

print(f"\nThe code took {finishTime-startTime} seconds, to run!")
