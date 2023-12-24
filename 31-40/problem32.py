from time import time

start = time()

digits = "123456789"
fullList = []
isPan = []
prods = set()

for a in range(1,10001):
    for b in range(1,10001):
        num = "".join([str(a),str(b),str(a*b)])
        if a*b>9999:
            break
        if len(num)==9:
            fullList.append(num)
            
for i in fullList:
    iSplit = list(i)
    iSplit.sort()
    iSplit = "".join(iSplit)
    if iSplit==digits:
        isPan.append(i)
            
for val in isPan:
    joiner = int("".join([val[-4],val[-3],val[-2],val[-1]]))
    prods.add(joiner)
    
end = time()
    
print(sum(prods))
print(f"{end-start} seconds")
        
