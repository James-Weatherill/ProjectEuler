from time import time
from math import isqrt

########################################

start_time = time()

########################################

def d(val):
    divisors = set()
    divisors.add(1)

    val_isqrt = isqrt(val)

    for divisor in range(val_isqrt, 1, -1):
        if val % divisor == 0:
            divisors.add(divisor)
            divisors.add(val // divisor)

    return sum(divisors)

nums_d_val = dict()

for num in range(1, 10_000):
    nums_d_val[num] = d(num)

ans = 0
for key in nums_d_val.keys():
    val = nums_d_val[key]

    if val >= 10_000:
        continue
    elif nums_d_val[key] == val and nums_d_val[val] == key and key != val and key < val:
        ans += (key + val)

print(f"\nThe sum of all amicable numbers under 10,000 is: {ans}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run\n")
