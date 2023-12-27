#! /opt/homebrew/bin/python3

from time import time
from copy import deepcopy as copy

startTime = time()

########################################

fixedList = []
file1 = open("assets/0059_cipher.txt", "r")
fileReadList = str(file1.readlines()).replace("['", "").replace("']", "").replace("\\n", "").split(",")
for item in fileReadList:
    fixedList.append(int(item))

########################################

tempLetters = []
savedTempLetters = []
finalCounter = 0
counter = 0
letter1 = "a"
letter2 = "b"
letter3 = "c"

correct = True

letters = "abcdefghijklmnopqrstuvwxyz"
allValidLetters = " :;,-.!?'()[]+/\"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            counter = 0
            correct = True
            newScore = 0
            tempLetters = [ord(letter1), ord(letter2), ord(letter3)] * 485
            for i in range(len(fixedList)):
                xorNum = tempLetters[i] ^ fixedList[i]
                if chr(xorNum) not in allValidLetters:
                    correct = False
                    break
                counter += xorNum
            if correct:
                break
        if correct:
            break
    if correct:
        finalCounter = counter
        break

if correct:
    finalStr = "".join([chr(fixedList[i] ^ tempLetters[i]) for i in range(1455)])
    print(f"The key letters are:\n1: {letter1}\n2: {letter2}\n3: {letter3}\n")
    print(f"{finalStr}\n")
    print(finalCounter)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

