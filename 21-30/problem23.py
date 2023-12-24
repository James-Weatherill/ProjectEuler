import numpy as np
from time import time

start = time()

allNums = set(np.arange(1, 28123))
run = 0

abundantNums = set()
for i in range(2,28123):
    half = i // 2
    run += 1
    for j in range(2, half+1):
        if i%j==0 and i!=j:
            run += j
    if run>i:
        abundantNums.add(i)
    run = 0
abundantNums = list(abundantNums)

abundantSums = set()
for i, num1 in enumerate(abundantNums):
    for num2 in abundantNums[i:]:
        numSum = num1+num2
        if num1+num2 > 28122:
            break
        else:    
            abundantSums.add(num1+num2)
    
final = list(allNums - abundantSums)

print(sum(final))

end = time()

print(f"\nThe program took: {round(end-start, 3)} seconds!\n")

final.sort()
print(final)

