from sympy import isprime
from time import time

start = time()

circPrime = set()
num = 0
while True:
    num += 1
    numList = list(str(num))
    tempList = []
    for i in range(len(numList)):
        circNum = numList[i:] + numList[:i]
        tempList.append(circNum)
    for j in tempList:
        cp = False
        if isprime(int("".join(j))):
            cp = True
        else:
            break
    if cp:
        circPrime.add("".join(tempList[0]))
    if num==999999:
        break
print(len(circPrime))

end = time()

print(f"{end-start} seconds!")
        
