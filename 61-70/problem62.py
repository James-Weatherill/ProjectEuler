#! /opt/homebrew/bin/python3

########################################

from time import time

########################################

startTime = time()

numberOfPermutations = 6

allNums = {}

counter = 1

while True:
    counterCube = counter**3
    sortedCounterCube = "".join(sorted(list(str(counterCube))))

    if sortedCounterCube in allNums:
        allNums[sortedCounterCube][0] += 1
        allNums[sortedCounterCube][1].append(counterCube)
    else:
        allNums[sortedCounterCube] = [1, [counterCube]]

    if allNums[sortedCounterCube][0] == numberOfPermutations:
        break

    counter += 1

isolatedList = allNums[sortedCounterCube][1]
finalStr = "\n".join([f"{i+1}) {round(isolatedList[i]**(1/3))} -> {str(isolatedList[i])}" for i in range(len(isolatedList))])

print(f"\nAll possible permutations:\n\n{finalStr}")

finishTime = time()

########################################

print(f"\nThe code took: {finishTime-startTime} seconds, to run!\n")
