from fractions import Fraction
from time import time

start = time()

quoteList = []
numerator = 1
denominator = 1
result = 1

for i in range(10,100):
    j = i+1
    while j<100:
        if i>=j:
            break
        else:
            iStr = str(i)
            jStr = str(j)
            common = set(iStr) & set(jStr)
            for c in common:
                iStr = iStr.replace(c,"")
                jStr = jStr.replace(c,"")
            if len(iStr)==1 and len(jStr)==1:
                if str(i)[-1]!="0" and str(j)[-1]!="0":
                    if i/j==int(iStr)/int(jStr):
                        numerator *= i
                        denominator *= j
        j += 1
        
end = time()
        
print(Fraction(numerator,denominator))
print(f"\n{end-start} seconds!")
    
