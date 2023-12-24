digitSum = [0,0,0]

for a in range(1,100):
    for b in range(1,100):
        tempSum = 0
        digitSplit = list(str(a**b))
        for digit in digitSplit:
            tempSum += int(digit)
        if tempSum>digitSum[0]:
            digitSum = [tempSum,a,b]
            
print(digitSum)
        
