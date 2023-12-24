from sympy import factorint
from time import time

start = time()

numList = [0]
i = 100_000

while len(numList)!=4:
    primes = []
    i += 1
    for _,prime in enumerate(factorint(i)):
        primes.append(prime)
    if len(primes)==4 and numList[-1]==i-1:
        numList.append(i)
    elif len(primes)==4:
        numList = [i]
        
end = time()
            
print(numList)
print(f"{end-start} seconds!")
