totalList = [1,2]
sumList = []

i = 0
val = 2
while val<4000000:
    totalList.append(totalList[i]+totalList[(i+1)])
    val = totalList[-1]
    i += 1

if val>4000000:
    del totalList[-1]
    
print(totalList)

length = int(len(totalList))
for j in range(length):
    if totalList[j]%2==0:
        sumList.append(totalList[j])
    
print(sumList)
print(sum(sumList))
