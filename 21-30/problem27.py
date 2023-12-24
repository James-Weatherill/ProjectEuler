from sympy import isprime
from time import time

start = time()

num = 0
b,c,length = 0,0,0

for i in range(-999,1000,1):
    for j in range(1,997,1):
        while True:
            if isprime(j)==False:
                break
            form = num**2 + i*(num) + j
            if isprime(form):
                num += 1
            else:
                break
        if length<num:
            b,c,length = i,j,num
        num = 0
        
end = time()
            
print(f"""Coefficients: b = {b} and c = {c}...
The formula that creates the longest chain ({length} primes) is:

    n\u00B2 - {abs(b)}n + {c}
""")

print(f"It took {end-start} seconds!")
