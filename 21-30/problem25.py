from time import time

start = time()

fibList = [1, 2]
for i in fibList:
    fibList.append(fibList[fibList.index(i)] + fibList[fibList.index(i) + 1])
    if len(str(fibList[fibList.index(i)+2]))>=1000:
        break
print((fibList.index(i)+2)+2)

end = time()

print(f"\nTime taken to calculate first Fibonacci number with >1000 digits:\n{end-start} seconds!")

