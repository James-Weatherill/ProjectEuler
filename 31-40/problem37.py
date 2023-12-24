from sympy import isprime
from time import time

startTime = time()

numList = []
primeList = []

for i in range(1,1000000):
    if i%2!=0 and i>10:
        numList.append(i)     
for num in numList:
    prime = True
    val = str(num)
    end = len(val)
    while True:
        if isprime(int(val)):
            val = val[:end]
            end -= 1
        else:
            prime = False
            break
        if end==-1:
            break
    if prime:
        val = str(num)
        start = 0
        while True:
            if isprime(int(val)):
                val = str(num)[start:]
                start += 1
            else:
                prime = False
                break
            if start==len(str(num))+1:
                break
        if prime:
            primeList.append(num)   
print(sum(primeList))

endTime = time()

print(f"{endTime-startTime} seconds")
