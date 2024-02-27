#! /opt/homebrew/bin/python3

########################################

from time import time

########################################

startTime = time()

eList = []
counter = 1
for i in range(33):
    eList = eList + [1, counter * 2, 1]
    counter += 1

ansList = [[1, eList[-1]]]

for i in range(len(eList)-2, -1, -1):
    ansList.append([ansList[-1][1], eList[i] * ansList[-1][1] + ansList[-1][0]])

ans = sum(int(x) for x in list(str(ansList[-1][1] * 2 + ansList[-1][0])))

print(ans)

finishTime = time()

########################################

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")
