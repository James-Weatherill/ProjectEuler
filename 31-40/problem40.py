from time import time

start = time()

num = ""
for i in range(1,185186):
    num += str(i)
indexProd = int(num[0]) * int(num[99]) * int(num[999]) * int(num[9999]) * int(num[99999]) * int(num[999999])

end = time()

print(indexProd)
print(f"{end-start} seconds!")
