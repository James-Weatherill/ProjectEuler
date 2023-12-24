from math import sqrt

Correct = False

sqList = []
num = 0
num2 = 0

for i in range(1,1000):
    sqList.append(i**2)

for num in sqList:
    for num2 in sqList:
        if (sqrt(num)+sqrt(num2)+sqrt(num+num2))==1000:
            Correct = True
            break
    if Correct:
        break
        
print(int(sqrt(num)*sqrt(num2)*(sqrt(num+num2))))
