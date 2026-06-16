from time import time

########################################

start_time = time()

########################################

total = 0
cur_nums = [1, 2, 3]

while cur_nums[2] <= 4_000_000:
    if cur_nums[0] % 2 == 0:
        total += cur_nums[0]

    cur_nums[0] = cur_nums[1]
    cur_nums[1] = cur_nums[2]
    cur_nums[2] = cur_nums[0] + cur_nums[1]

if cur_nums[0] % 2 == 0:
    total += cur_nums[0]

if cur_nums[1] % 2 == 0:
    total += cur_nums[1]

print(f"\nThe sum of Fibonacci Sequence values <= 4,000,000... is: {total}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
