from math import sqrt
from statistics import mode
from time import time

start = time()

triList = []
for a in range(1,500):
    for b in range(1,500):
        c = sqrt(a**2 + b**2)
        if a%1==0 and b%1==0 and c%1==0 and (a+b+c)<=1000:
            triList.append([a,b,int(c)])           
for num in triList:
    triList[triList.index(num)] = sum(num)    
print(mode(triList))

end = time()

print(f"{end-start} seconds")

