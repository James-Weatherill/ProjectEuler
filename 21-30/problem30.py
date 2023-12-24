from time import time

start = time()

tempList = []
numList = []
for i in range(2,1000000):
    breakUp = list(str(i))
    for j in breakUp:
        tempList.append(int(j)**5)
    if sum(tempList)==i:
        numList.append(i)
    tempList = []
    
end = time()
    
print(sum(numList))
print(f"{end-start} seconds")

