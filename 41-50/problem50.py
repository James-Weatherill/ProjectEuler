from sympy import isprime

primes = []
numInd = [0,0,0]
length = 0
count = -1

for i in range(1,100_000):
    if isprime(i):
        primes.append(i)
        
while True:
    count += 1
    length = 0
    ind = count
    sumList = []
    num = 0
    while True:
        ind += 1
        num += primes[ind]
        sumList.append(primes[ind])
        if isprime(num):
            length += 1
        if num>=1_000_000:
            break
        if isprime(num) and num>=numInd[0] and length>numInd[2]:
            numInd = [num,ind,length]
        if ind==9591:
            break
    if count==9590:
        break
        
print(numInd)

