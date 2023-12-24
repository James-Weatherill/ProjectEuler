from sympy import primerange
from math import sqrt

goodNums = []

num = 600851475143

primeList = list(primerange(2, int(sqrt(num))+1))

for i in primeList:
    if num%i==0:
        goodNums.append(i)
        
print(goodNums)
