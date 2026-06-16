import os
from time import time

########################################

start_time = time()

########################################

assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
file_path = os.path.join(assets_path, "0018_data.txt")

with open(file_path, "r+") as file:
    tri_rows = [[int(val) for val in row.replace("\n", "").split(" ")] for row in file.readlines()]

for row_idx in range(len(tri_rows) - 2, -1, -1):
    for val_idx in range(len(tri_rows[row_idx])):
        if tri_rows[row_idx + 1][val_idx] >= tri_rows[row_idx + 1][val_idx + 1]:
            tri_rows[row_idx][val_idx] += tri_rows[row_idx + 1][val_idx]
        else:
            tri_rows[row_idx][val_idx] += tri_rows[row_idx + 1][val_idx + 1]

print(f"\nThe greatest sum of numbers from top to bottom is: {tri_rows[0][0]}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
