from time import time

start = time()

numSum = 0
for i in range(1,1001):
    numSum += i**i
length = len(str(numSum))
last10 = str(numSum)[length-10:length]

end = time()

print(last10)
print(f"{end-start} seconds!")
