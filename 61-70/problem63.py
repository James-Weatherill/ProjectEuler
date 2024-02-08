#! /opt/homebrew/bin/python3

########################################

from time import time

########################################

startTime = time()

counter = 0
on = True

curNum = 1
power = 1

while True:

    couPowStr = str(counter**power)

    if len(couPowStr) == power and not on:
        on = True
        counter += 1
        power += 1
    elif len(couPowStr) != power and on:
        on = False
        power = 1
        curNum = 1
    elif len(couPowStr) == power and on:
        counter += 1
        power += 1

    if counter%1_000 == 0:
        print(counter)

finishTime = time()

########################################

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")
