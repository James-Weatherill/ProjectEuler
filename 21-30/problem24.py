from math import factorial as fact
from itertools import permutations
from time import time

start = time()

orderSet = set()
numList = [0,1,2,3,4,5,6,7,8,9]

for i in permutations(numList):
    orderSet.add(i)
        
orderList = list(orderSet)
orderList.sort()
print(orderList[999999])

end = time()

print(f"\nIt took {end-start} seconds to calculate the 1,000,000 permutation!")

