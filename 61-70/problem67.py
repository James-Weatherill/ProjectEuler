import os
from time import time

########################################

startTime = time()

########################################

filePath = os.path.join(os.getcwd(), "61-70", "assets", "0067_triangle.txt")

with open(filePath, "r") as file:
    fileRead = file.readlines()

rowsList = [[int(num) for num in row.replace("\n", "").split(" ")] for row in fileRead]

for row in range(98, -1, -1):
    for col in range(0, row + 1):
        rowsList[row][col] += max(rowsList[row + 1][col], rowsList[row + 1][col + 1])

print(f"\nMaximum path sum: {rowsList[0][0]}")

########################################

finishTime = time()
print(f"\nThe code took: {finishTime - startTime} seconds, to run!\n")

########################################
