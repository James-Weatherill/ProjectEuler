from time import time
from math import isqrt, sqrt

########################################

startTime = time()

########################################

nums = [val for val in range(1, 1001) if sqrt(val)%1 != 0]

highestX = 0
matchingD = 0
trailingY = 0

for num in nums:
    howDeep = 1
    while True:
        allIntegers = []
        testNum = num
        integerRoot = isqrt(testNum)
        allIntegers.append(integerRoot)

        numerator = "1"
        denominator = f"-{integerRoot}"

        for i in range(howDeep):
            tempDivisor = int(numerator)

            numerator = denominator
            numerator = numerator.replace("-", "+")
            denomMinLoc = denominator.find("-")
            denominator = f"{int((testNum - int(denominator[denomMinLoc+1:])**2) / tempDivisor)}"

            toAppend = int((sqrt(testNum) + int(numerator)) / int(denominator))
            allIntegers.append(toAppend)

            numerator = f"{int(numerator) - toAppend * int(denominator)}"

            tempVar = numerator
            numerator = denominator
            denominator = tempVar

        numerator = 1
        denominator = allIntegers[-1]
        allIntegers = allIntegers[:-1]

        while True:
            tempVar = numerator
            numerator = (allIntegers[-1] * denominator) + numerator

            if len(allIntegers) == 1:
                break

            allIntegers = allIntegers[:-1]

            tempVar = numerator
            numerator = denominator
            denominator = tempVar

        if (numerator**2 - (testNum * denominator**2) == 1):
            if highestX < numerator:
                highestX = numerator
                matchingD = testNum
                trailingY = denominator
            break

        howDeep += 1

print(f"\nHighest x value: {highestX},\nmatching D value: {matchingD},\n(with a trailing y value: {trailingY})")

########################################

finishTime = time()
print(f"\nThe code took: {finishTime - startTime} seconds, to run!\n")

########################################
