from time import time
from math import isqrt

########################################

start_time = time()

########################################

def is_prime(val):
    if val % 2 == 0:
        return False

    val_isqrt = isqrt(val)
    if val_isqrt % 2 == 0:
        val_isqrt -= 1

    for i in range(val_isqrt, 2, -2):
        if val % i == 0:
            return False

    return True

cur_total = 2 + 3 + 5 + 7

for prime in range(11, 2_000_000, 2):
    if is_prime(prime):
        cur_total += prime

print(f"\nThe sum of all primes below 2,000,000, is: {cur_total}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} to run!\n")
