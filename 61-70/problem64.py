#! /opt/homebrew/bin/python3

########################################

from time import time
from math import sqrt

########################################

startTime = time()

fullList = []

num = 23
numerator = 1

truncNum = int(sqrt(num))
denominator = sqrt(num)-truncNum
prevTerm = numerator/denominator

for i in range(1, 8):

    flippedDenom = (-1)*(denominator-sqrt(num))+sqrt(num)

    numerator = numerator*flippedDenom
    denominator = denominator*flippedDenom
    tempTerm = numerator/denominator

    separateInt = int(tempTerm)
    fullList.append(separateInt)

    prevTerm = tempTerm-separateInt

print(fullList)

finishTime = time()

########################################

print(f"The code took: {finishTime-startTime} seconds, to run!")
