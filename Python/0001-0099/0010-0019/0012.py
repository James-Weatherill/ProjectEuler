from time import time
from math import isqrt

########################################

start_time = time()

########################################

def num_of_divisors(val):
    tally = 0

    val_isqrt = isqrt(val)

    if val_isqrt**2 == val:
        tally += 1
        val_isqrt -= 1

    if val_isqrt != 0:
        for divisor in range(1, val_isqrt + 1):
            if val % divisor == 0:
                tally += 2

    return tally

increment = 1
cur_tri_num = 1

while True:
    increment += 1
    cur_tri_num += increment

    if num_of_divisors(cur_tri_num) > 500:
        break

print(f"\nThe first triangular number with more\nthan 500 divisors, is: {cur_tri_num}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
