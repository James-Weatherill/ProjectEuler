from time import time

########################################

start_time = time()

########################################

largest_palindrome = 0

for first_num in range(100, 1000):
    for second_num in range(first_num, 1000):
        product = first_num * second_num

        prod_str_forward = str(product)
        prod_str_backward = prod_str_forward[::-1]

        if (prod_str_forward == prod_str_backward) and (product > largest_palindrome):
            largest_palindrome = product

print(f"\nThe largest palindrome formed by the product of\ntwo 3 digit integers, is: {largest_palindrome}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
