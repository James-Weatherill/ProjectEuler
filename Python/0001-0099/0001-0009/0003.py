from time import time
from math import isqrt

########################################

start_time = time()

########################################

def is_prime(val):
    if val % 2 == 0:
        return False

    val_isqrt = isqrt(val)

    for i in range(val_isqrt, 2, -1):
        if val % i == 0:
            return False
        
    return True

########################################

# test_num = 13_195
test_num = 600_851_475_143
test_num_storage = test_num

highest_prime_divisor = 0

for prime in range(2, 600_851_475_144):
    if is_prime(prime):
        while True:
            if test_num % prime == 0:
                print(f"{test_num} -> (by {prime})")
                test_num //= prime

                if prime > highest_prime_divisor:
                    highest_prime_divisor = prime
            else:
                break
    if test_num == 1:
        break

print(f"\nThe highest prime factor of {test_num_storage}, is: {highest_prime_divisor}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
