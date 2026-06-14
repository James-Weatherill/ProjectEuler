import os
from time import time

########################################

start_time = time()

########################################

assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
file_path = os.path.join(assets_path, "0008_data.txt")

with open(file_path, "r+") as file:
    value_str = file.read().strip()

subnum_length = 13

best_prod = 0
best_prod_subnum = []

for idx in range(subnum_length, 1000):
    cur_prod = 1

    first_idx = (idx - subnum_length) + 1
    last_idx = idx

    for val_idx in range(first_idx, last_idx + 1):
        cur_prod *= int(value_str[val_idx])

    if cur_prod > best_prod:
        best_prod = cur_prod
        best_prod_subnum = [value_str[val_idx] for val_idx in range(first_idx, last_idx + 1)]

print(f"""\nThe greatest product: {best_prod}, is achieved finding
the product of the adjacent numbers: {"".join(best_prod_subnum)}""")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} to run!\n")
