from string import ascii_uppercase
from time import time

start = time()

numTriWords = 0

file = open("assets/0042_words.txt", "r+")
rFile = (str(file.readlines()).replace("['","").replace("']","").replace(":","")).split(",")

triNums = []
curNum = 0
for a in range(1,25):
    curNum += a
    triNums.append(curNum)

for word in rFile:
    wordTot = 0
    for letter in word:
        wordTot += (ascii_uppercase.index(letter) + 1)
    if wordTot in triNums:
        numTriWords += 1
        
end = time()
        
print(numTriWords)
print(f"{end-start} seconds!")

