from time import time

########################################

start_time = time()

########################################

def collatz_calc(val):
    counter = 1

    while val != 1:
        if val % 2 == 0:
            val //= 2
            counter += 1
        else:
            val = (3 * val) + 1
            counter += 1

    return counter

top_chain_len = 0
top_chain_len_num = 0

for num in range(1, 1_000_000):
    cur_collatz_chain_len = collatz_calc(num)

    if cur_collatz_chain_len > top_chain_len:
        top_chain_len = cur_collatz_chain_len
        top_chain_len_num = num

print(f"""\nFor Natural numbers below one million ...
The value: {top_chain_len_num},
produces the longest chain length: {top_chain_len}""")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
