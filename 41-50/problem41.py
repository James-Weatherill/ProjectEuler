from sympy import isprime
from time import time

start = time()

result = 0
for a in range(5000000,10000000):
    if isprime(a):
        lenNums = ""
        aLen = len(str(a))
        for b in range(1,aLen+1):
            lenNums += str(b)
        temp = "".join(sorted(str(a)))
        if temp==lenNums:
            if a>result:
                result = a
                
end = time()
                
print(result)
print(f"{end-start} seconds!")

