from math import sqrt
from time import time

start = time()

def ispentagonal(x: int) -> bool:
    if type((sqrt(24*x + 1) + 1) / 6) == int:
        isPent = 1
    else:
        isPent = 0
    return isPent

pentNums = []
for i in range(2500,0,-1):
    pentNums.append(i*(3*i - 1)/2)
for num1 in pentNums:
    for num2 in pentNums[pentNums.index(num1)+1:]:
        numSum = num1+num2
        numMin = abs(num1-num2)
        if ispentagonal(numSum) and ispentagonal(numMin):
            ans = numMin
            
end = time()

print(int(ans))
print(f"{end-start} seconds")
