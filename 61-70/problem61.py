#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

def triangleNums(inputNum):
    n = int(inputNum)
    return str((n*(n+1))//2)

def squareNums(inputNum):
    n = int(inputNum)
    return str(n**2)

def pentagonalNums(inputNum):
    n = int(inputNum)
    return str((n*(3*n-1))//2)

def hexagonalNums(inputNum):
    n = int(inputNum)
    return str(n*(2*n-1))

def heptagonalNums(inputNum):
    n = int(inputNum)
    return str((n*(5*n-3))//2)

def octagonalNums(inputNum):
    n = int(inputNum)
    return str(n*(3*n-2))

n = 0
found = False

triangleList = []
squareList = []
pentagonalList = []
hexagonalList = []
heptagonalList = []
octagonalList = []

while True:
    n += 1

    if len(triangleNums(n)) == 4:
        triangleList.append(triangleNums(n))

    elif len(triangleNums(n)) == 5:
        break

    if len(squareNums(n)) == 4:
        squareList.append(squareNums(n))

    if len(pentagonalNums(n)) == 4:
        pentagonalList.append(pentagonalNums(n))

    if len(hexagonalNums(n)) == 4:
        hexagonalList.append(hexagonalNums(n))

    if len(heptagonalNums(n)) == 4:
        heptagonalList.append(heptagonalNums(n))

    if len(octagonalNums(n)) == 4:
        octagonalList.append(octagonalNums(n))

listOfLists = [triangleList, squareList, pentagonalList, hexagonalList, heptagonalList, octagonalList]

for list1 in listOfLists:

    for num1 in list1:
        num1Start = str(num1)[0:2]
        num1End = str(num1)[2:4]

        for list2 in listOfLists:
            if list2 != list1:

                for num2 in list2:
                    num2Start = str(num2)[0:2]
                    num2End = str(num2)[2:4]

                    if num1End == num2Start:

                        for list3 in listOfLists:
                            if list3 != list1 and list3 != list2:

                                for num3 in list3:
                                    num3Start = str(num3)[0:2]
                                    num3End = str(num3)[2:4]

                                    if num2End == num3Start:

                                        for list4 in listOfLists:
                                            if list4 != list1 and list4 != list2 and list4 != list3:

                                                for num4 in list4:
                                                    num4Start = str(num4)[0:2]
                                                    num4End = str(num4)[2:4]

                                                    if num3End == num4Start:

                                                        for list5 in listOfLists:
                                                            if list5 != list1 and list5 != list2 and list5 != list3 and list5 != list4:

                                                                for num5 in list5:
                                                                    num5Start = str(num5)[0:2]
                                                                    num5End = str(num5)[2:4]

                                                                    if num4End == num5Start:

                                                                        for list6 in listOfLists:
                                                                            if list6 != list1 and list6 != list2 and list6 != list3 and list6 != list4 and list6 != list5:

                                                                                for num6 in list6:
                                                                                    num6Start = str(num6)[0:2]
                                                                                    num6End = str(num6)[2:4]
                                                                                    
                                                                                    if num5End == num6Start and num6End == num1Start:
                                                                                        found = True
                                                                                    if found:
                                                                                        break
                                                                            if found:
                                                                                break
                                                                    if found:
                                                                        break
                                                            if found:
                                                                break
                                                    if found:
                                                        break
                                            if found:
                                                break
                                    if found:
                                        break
                            if found:
                                break
                    if found:
                        break
            if found:
                break
        if found:
            break
    if found:
        break

if found:
    print(num1, num2, num3, num4, num5, num6)
    print(int(num1) + int(num2) + int(num3) + int(num4) + int(num5) + int(num6))

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

