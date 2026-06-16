from time import time

########################################

start_time = time()

########################################

lower_bound = 1
upper_bound = 1000

nums_list = [i for i in range(lower_bound, upper_bound)]

ans = sum(val for val in nums_list if (val % 3 == 0 or val % 5 == 0))

print(f"\nThe sum of values divisible by 3 OR 5 between {lower_bound} and {upper_bound}, is: {ans}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
