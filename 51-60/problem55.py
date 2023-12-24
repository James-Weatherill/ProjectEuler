Lychrel = 0

for i in range(10,10_000):
    pal = False
    num = str(i)
    numRev = str(i)[::-1]
    for times in range(50):
        curNum = str(int(num)+int(numRev))
        if curNum==curNum[::-1]:
            pal = True
        num = curNum
        numRev = curNum[::-1]
    if not pal:
        Lychrel += 1
        
print(Lychrel)
        
