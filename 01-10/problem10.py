from math import sqrt

primesList = []

for i in range(1,2000001):
    prime = True
    squareRoot = int(sqrt(i))
    while squareRoot>1:
        if i%squareRoot==0:
            prime = False
            break
        else:
            squareRoot -= 1
    if prime:
        primesList.append(i)
            
print(sum(primesList))
