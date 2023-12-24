from sympy import factorint

add = 1
addT = 1

while True:
    add += 1
    addT += add
    total = 1
    powers = []
    setOfFacs = factorint(addT)
    for a,b in setOfFacs.items():
        powers.append(b)
    for i in range(0, len(powers)):
        powers[i] = powers[i]+1
    for nums in powers:
        total *= nums
    if total>500:
        break
        
print(addT)

