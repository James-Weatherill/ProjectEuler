import os
from time import time

########################################

start_time = time()

########################################

assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
file_path = os.path.join(assets_path, "0013_data.txt")

with open(file_path, "r+") as file:
    nums = [int(num.strip()) for num in file.readlines()]

nums_sum_str = str(sum(num for num in nums))

print(f"\nThe first ten digits of the sum are: {nums_sum_str[:10]}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
