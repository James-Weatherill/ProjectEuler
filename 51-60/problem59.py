#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("assets/0059_cipher.txt", "r")
fileReadList = str(file1.readlines()).replace("['", "").replace("']", "").split(",")
for item in fileReadList:
    fixedList.append(bin(int(item))[2:].zfill(7))

########################################



########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

