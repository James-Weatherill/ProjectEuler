import numpy as np

rows = 12
cols = 6
arrayStack = np.empty((rows+1,cols+1))

colsList = []
totList = []

for a in range(cols+1):
    colsList.append(1)
    
for b in range(rows+1):
    totList.append(colsList)
totArr = np.array(totList)

for i in range(1,(rows+1)):
    for j in range(1,(cols+1)):
        totArr[i,j] = totArr[i-1,j] + totArr[i,j-1]

# print(totArr)
print(totArr[rows,cols])
