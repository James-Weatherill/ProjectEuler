#! /opt/homebrew/bin/python3

########################################

from time import time

########################################

startTime = time()

counter = 0

for i in range(1,10):
    power = 1
    while power<22:
        numPowStr = str(i**power)
        if len(numPowStr) == power:
            counter += 1
            power += 1
        else:
            power += 1

print(counter)

finishTime = time()

########################################

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")
