from time import time

start = time()

one2nine = "123456789"
len9List = []
ind = -1

for i in range(2,10000):
    multiplier = 1
    concatProd = []
    while True:
        concatProd.append(str(i*multiplier))
        concatStr = "".join(concatProd)
        if len(concatStr)>9:
            break
        elif len(concatStr)==9:
            len9List.append(concatStr)
            break
        else:
            multiplier += 1
while True:
    len9List.sort()
    val = list(len9List[ind])
    val.sort()
    val = "".join(val)
    if val==one2nine:
        print(len9List[ind])
        break
    ind -= 1
    
end = time()

print(f"{end-start} seconds")
        
