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

# 2, 3, 5, 7, 11
num = 11
counter = 4

while True:
    if is_prime(num):
        counter += 1
    if counter == 10_001:
        break
    num += 2

print(f"\nThe 10,001st prime is: {num}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} to run!\n")