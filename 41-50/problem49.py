from sympy import isprime
from time import time

start = time()

fourDigits = []
for i in range(1000,10000):
    if isprime(i):
        fourDigits.append(i)
        
for num in fourDigits[:]:
    if (num+3330) not in fourDigits or (num+6660) not in fourDigits or ("".join(sorted(str(num))))!=("".join(sorted(str(num+3330)))) or ("".join(sorted(str(num))))!=("".join(sorted(str(num+6660)))):
        fourDigits.remove(num)
        
twelve = str(fourDigits[-1]) + str(fourDigits[-1] + 3330) + str(fourDigits[-1] + 6660)

end = time()
        
print(twelve)
print(f"{end-start} seconds!")
