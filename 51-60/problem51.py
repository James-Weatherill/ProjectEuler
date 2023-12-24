from sympy import isprime
from time import time

start = time()

primes = []
permSet = set()

for a in range(100_000,1_000_000):
    if isprime(a):
        primes.append(a)
        
for prime in primes:
    primeStr = str(prime)
    one = primeStr[0]
    two = primeStr[1]
    three = primeStr[2]
    four = primeStr[3]
    five = primeStr[4]
    six = primeStr[5]
    un = "_"
    permSet.add(one + two + three + un + un + un)
    permSet.add(un + two + three + four + un + un)
    permSet.add(un + un + three + four + five + un)
    permSet.add(un + un + un + four + five + six)
    permSet.add(one + two + un + four + un + un)
    permSet.add(un + two + three + un + five + un)
    permSet.add(un + un + three + four + un + six)
    permSet.add(one + two + un + un + five + un)
    permSet.add(un + two + three + un + un + six)
    permSet.add(one + un + three + un + five + un)
    permSet.add(un + two + un + four + un + six)
    permSet.add(one + un + un + four + five + un)
    permSet.add(un + un + three + four + un + six)
    permSet.add(one + two + un + un + five + un)
    permSet.add(one + un + un + four + un + six)
    permSet.add(un + un + three + un + five + six)
    permSet.add(one + two + three + un + un + un)
    permSet.add(one + two + un + un + un + six)
    permSet.add(one + un + un + un + five + six)
    permSet.add(un + un + un + four + five + six)
    
permList = list(permSet)

for perm in permList:
    count = 0
    for i in range(0,10):
        val = perm.replace("_",str(i))
        if isprime(int(val)) and len(str(int(val)))==6:
            if count==0:
                missing = str(i)
            count += 1
    if count==8:
        print(perm.replace("_",missing))
        
end = time()

print(f"{end-start} seconds!")

