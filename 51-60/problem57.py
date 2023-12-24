from fractions import Fraction
from time import time

start = time()

total = 0

for i in range(999):
    div = 2+Fraction(1,2)
    if i>0:
        for i in range(i):
            div = 2+Fraction(1/div)
    ans = 1+Fraction(1,div)
    if len(str(ans.numerator))>len(str(ans.denominator)):
        total += 1
        
end = time()
        
print(total)
print(f"{end-start} seconds!")

