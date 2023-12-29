#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

numList = []

for i in range(1,1000):
    if i%3==0:
        numList.append(i)
    elif i%5==0:
        numList.append(i)

total = sum(numList)
print(total)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")
        