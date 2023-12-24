from math import sqrt
from time import time

start = time()

hexList = []

def istri(x: int) -> bool:
    num = (-1 + sqrt(8*x + 1))/2
    if num%1==0:
        return 1
    else:
        return 0
    
def ispent(x: int) -> bool:
    num = (sqrt(24*x + 1) + 1)/6
    if num%1==0:
        return 1
    else:
        return 0 
    
def ishex(x: int) -> bool:
    num = (sqrt(8*x + 1) + 1)/4
    if num%1==0:
        return 1
    else:
        return 0
    
for i in range(1,30000):
    hexList.append(i*(2*i -1))
    
for i in hexList:
    if ispent(i):
        result = i
        
end = time()
        
print(result)
print(f"{end-start} seconds!")

