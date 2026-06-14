from time import time

########################################

start_time = time()

########################################

first_100_nat_num = [val for val in range(1, 101)]

sum_of_squares = sum(val**2 for val in first_100_nat_num)
square_of_sum = (sum(first_100_nat_num))**2

print(f"""\nFor the Natural numbers: 1, 2, ..., 100, the...
Sum of squares => 1^(2) + 2^(2) + ... + 100^(2) = {sum_of_squares}, and...
Square of the sum => (1 + 2 + ... + 100)^(2) = {square_of_sum}, is...
|{sum_of_squares} - {square_of_sum}| = {abs(sum_of_squares - square_of_sum)}""")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} to run!\n")
