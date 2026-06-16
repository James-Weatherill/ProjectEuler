from time import time
from math import factorial

########################################

start_time = time()

########################################

grid_size = 20

# There are two options: down (D) or right (R)
# => combinations for 2x2 = DDRR, DRDR, DRRD, RDDR, RDRD, RRDD = 6 combinations
# => No. combinations for nxn grid = (2n)C(n) = (2n)! / (n! * n!)

print(f"""\nThe number of ways to go from top-left
to bottom-right, on a {grid_size}x{grid_size} grid, is: {int(factorial(2 * grid_size) / (factorial(grid_size) * factorial(grid_size)))}""")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
