#! /opt/homebrew/bin/python3

########################################

from time import time
from mpmath import mp

########################################

startTime = time()

mp.dps = 100

eList = []
counter = 1
for i in range(3):
    eList = eList + [1, counter * 2, 1]
    counter += 1

print(eList)

finishTime = time()

########################################

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")
