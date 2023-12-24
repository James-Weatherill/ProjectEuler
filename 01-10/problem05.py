import numpy as np

found = []

num = 20
oneToTwenty = np.arange(1,21)

while len(found)==0:
    points = 0
    for i in oneToTwenty:
        if num%i==0:
            points += 1
        else:
            num += 1
            break
    if points==20:
        found.append(num)
            
print(found)
