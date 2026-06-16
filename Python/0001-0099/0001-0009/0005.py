from time import time

########################################

start_time = time()

########################################

test_num = 20

while True:
    evenly_divisible = True

    for divisor in range(3, 20):
        if test_num % divisor == 0:
            continue
        else:
            evenly_divisible = False
            break

    if evenly_divisible:
        break
    else:
        test_num += 20

print(f"\nThe smallest Natural number which is cleanly divisible\nby 1, 2, ..., 20 is: {test_num}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
