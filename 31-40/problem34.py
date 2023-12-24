from math import factorial as fact
from time import time

start = time()

factSum = []
totalList = []
for i in range(3,50000):
    iSplit = list(str(i))
    for num in iSplit:
        factSum.append(fact(int(num)))
    if sum(factSum)==i:
        totalList.append(i)
    factSum = []
totalSum = sum(totalList)

end = time()

print(totalList)
print(totalSum)
print(f"{end-start} seconds")

