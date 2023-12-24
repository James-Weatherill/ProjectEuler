from sympy import isprime
from time import time

start = time()

val = 0
doubleSquare = []
theNum = []
oddNonPrimes = []

while len(doubleSquare)!=50:
    val += 1
    doubleSquare.append(2*(val**2))

for i in range(2,6000):
    if isprime(i)==False and i%2!=0:
        oddNonPrimes.append(i)
        
for num in oddNonPrimes:
    ind = -1
    while True:
        ind += 1
        if isprime(num-doubleSquare[ind]):
            break
        if ind==49:
            theNum.append(num)
            break
            
end = time()
            
print(theNum)
print(f"{end-start} seconds")

