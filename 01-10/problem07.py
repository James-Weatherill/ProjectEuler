from math import sqrt, trunc

primes = []
num = 0
counter = 0

while counter < 10002:
    num += 1
    prime = True
    squareRoot = int(sqrt(num))
    while squareRoot>1:
        if num%squareRoot==0:
            prime = False
            break
        else:
            squareRoot -= 1
    if prime:
        primes = []
        counter += 1
        primes.append(num)

print(primes)
            
