from sympy import isprime
from time import time

start = time()

topR = []
topL = []
botL = []
botR = [1]
primes = 0
length = 0
diags = 1
ans = 1

while ans>=0.1:
    length += 2
    topR.append(botR[-1]+length)
    topL.append(topR[-1]+length)
    botL.append(topL[-1]+length)
    botR.append(botL[-1]+length)

    diags += 4

    if isprime(topR[-1]):
        primes += 1
    if isprime(topL[-1]):
        primes += 1
    if isprime(botL[-1]):
        primes += 1        
    if isprime(botR[-1]):
        primes += 1
            
    ans = primes/diags
    
length = length+1
    
end = time()

print(length)
print(f"{end-start} seconds!")

