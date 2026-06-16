import os
from time import time

########################################

start_time = time()

########################################

assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
file_path = os.path.join(assets_path, "0011_data.txt")

with open(file_path, "r+") as file:
    grid = file.readlines()
    grid = [[int(num) for num in row.replace("\n", "").split(" ")] for row in grid]

print("")

best_adj_prod = 0

# down
for row_idx in range(len(grid) - 3):
    for col_idx in range(len(grid[row_idx])):
        cur_num = grid[row_idx][col_idx] * grid[row_idx + 1][col_idx] * grid[row_idx + 2][col_idx] * grid[row_idx + 3][col_idx]
        
        if cur_num > best_adj_prod:
            print(f"Down: Row {row_idx + 1}, Column {col_idx + 1}  ->  {grid[row_idx][col_idx]} * {grid[row_idx + 1][col_idx]} * {grid[row_idx + 2][col_idx]} * {grid[row_idx + 3][col_idx]} = {cur_num}")
            best_adj_prod = cur_num

# right
for row_idx in range(len(grid)):
    for col_idx in range(len(grid[row_idx]) - 3):
        cur_num = grid[row_idx][col_idx] * grid[row_idx][col_idx + 1] * grid[row_idx][col_idx + 2] * grid[row_idx][col_idx + 3]
        
        if cur_num > best_adj_prod:
            print(f"Right: Row {row_idx + 1}, Column {col_idx + 1}  ->  {grid[row_idx][col_idx]} * {grid[row_idx][col_idx + 1]} * {grid[row_idx][col_idx + 2]} * {grid[row_idx][col_idx + 3]} = {cur_num}")
            best_adj_prod = cur_num

# down-right
for row_idx in range(len(grid) - 3):
    for col_idx in range(len(grid[row_idx]) - 3):
        cur_num = grid[row_idx][col_idx] * grid[row_idx + 1][col_idx + 1] * grid[row_idx + 2][col_idx + 2] * grid[row_idx + 3][col_idx + 3]
        
        if cur_num > best_adj_prod:
            print(f"Down-Right: Row {row_idx + 1}, Column {col_idx + 1}  ->  {grid[row_idx][col_idx]} * {grid[row_idx + 1][col_idx + 1]} * {grid[row_idx + 2][col_idx + 2]} * {grid[row_idx + 3][col_idx + 3]} = {cur_num}")
            best_adj_prod = cur_num

# down-left 
for row_idx in range(len(grid) - 3):
    for col_idx in range(3, len(grid[row_idx])):
        cur_num = grid[row_idx][col_idx] * grid[row_idx + 1][col_idx - 1] * grid[row_idx + 2][col_idx - 2] * grid[row_idx + 3][col_idx - 3]
        
        if cur_num > best_adj_prod:
            print(f"Down-Left: Row {row_idx + 1}, Column {col_idx + 1}  ->  {grid[row_idx][col_idx]} * {grid[row_idx + 1][col_idx - 1]} * {grid[row_idx + 2][col_idx - 2]} * {grid[row_idx + 3][col_idx - 3]} = {cur_num}")
            best_adj_prod = cur_num

print(f"\nThe highest product of four adjacent values from the grid, is: {best_adj_prod}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
