large = 0
long = 0

num = 0

while num<1000000:
    if long>large:
        numSav = num
        large = long
    long = 0
    num += 1
    nextNum = num
    while True:
        if nextNum%2==0:
            nextNum = (nextNum/2)
            long += 1
        elif nextNum%2!=0:
            nextNum = (3*nextNum)+1
            long += 1
        if nextNum==4 or nextNum==2 or nextNum==1:
            long += 2
            break
print(large)
print(numSav)
