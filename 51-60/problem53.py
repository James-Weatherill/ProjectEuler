from scipy.special import comb as ncr
from time import time

start = time()

count = 0
for n in range(1,101):
    for r in range(1,n+1):
        if ncr(n,r)>=1_000_000:
            count += 1
            
end = time()
            
print(count)
print(f"{end-start} seconds!")

