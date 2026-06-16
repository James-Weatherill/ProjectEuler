from time import time

########################################

start_time = time()

########################################

power = 1000

two_pow_str = str(2**power)

sum_of_digits = sum(int(digit) for digit in two_pow_str)

print(f"\nThe sum of the digits in 2^{power}, is: {sum_of_digits}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
