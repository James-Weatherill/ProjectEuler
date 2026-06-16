from time import time
from math import factorial as fact

########################################

start_time = time()

########################################

val_str = str(fact(100))

digit_sum = sum(int(char) for char in val_str)

print(f"\nThe sum of the digits in 100!, is: {digit_sum}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
