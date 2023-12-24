from time import time

start = time()

two2Four = []
five2Seven = []
eight2Ten = []
two2SevenTemp = []
two2Seven = []
two2TenTemp = []
two2Ten = []
one2Ten = []
one2TenPans = []

pand = "0123456789"

for a in range(100,1000):
    if a%2==0:
        two2Four.append(str(a))
    if a%7==0:
        five2Seven.append(str(a))
    if a%17==0:
        eight2Ten.append(str(a))
        
for num1 in two2Four:
    for num2 in five2Seven:
        two2SevenTemp.append(num1+num2)
        
for val in two2SevenTemp:
    threeVal = int(val[1]+val[2]+val[3])
    fiveVal = int(val[2]+val[3]+val[4])
    if threeVal%3==0 and threeVal>=3 and fiveVal%5==0 and fiveVal>=5:
        two2Seven.append(val)
        
for num1 in two2Seven:
    for num2 in eight2Ten:
        two2TenTemp.append(num1+num2)
        
for val in two2TenTemp:
    elevenVal = int(val[4]+val[5]+val[6])
    thirteenVal = int(val[5]+val[6]+val[7])
    if elevenVal%11==0 and elevenVal>=11 and thirteenVal%13==0 and thirteenVal>=13:
        two2Ten.append(val)
        
for num in two2Ten:
    for i in range(10):
        one2Ten.append(str(i)+num)
        
for nums in one2Ten:
    if "".join(sorted(nums))==pand:
        one2TenPans.append(int(nums))
        
pandigitalSum = sum(one2TenPans)
        
end = time()

print(pandigitalSum)
print(f"{end-start} seconds!")

