from time import time

start = time()

numList = []
for i in range(1,1000000):
    binary = bin(i)[2:]
    if str(i)==str(i)[::-1] and binary==binary[::-1]:
        numList.append(i)       
print(sum(numList))

end = time()

print(f"{end-start} seconds!")
        
