from time import time

########################################

start_time = time()

########################################

nums_as_letters_dict = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
                        10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
                        20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
                        100:"onehundred", 200:"twohundred", 300:"threehundred", 400:"fourhundred", 500:"fivehundred", 600:"sixhundred", 700:"sevenhundred", 800:"eighthundred", 900:"ninehundred"}

total_letters = 0

for num in range(1, 1000):
    num_str = str(num)

    if len(num_str) == 1:
        total_letters += len(nums_as_letters_dict[num])
    elif len(num_str) == 2 and num_str[0] == "1":
        total_letters += len(nums_as_letters_dict[num])
    elif len(num_str) == 2:
        tens = int(num_str[0]) * 10
        digit = int(num_str[1])

        total_letters += (len(nums_as_letters_dict[tens]) + len(nums_as_letters_dict[digit]))
    elif num_str[1] == "0" and num_str[2] == "0":
        hundreds = int(num_str[0]) * 100
        digit = int(num_str[2])

        total_letters += (len(nums_as_letters_dict[hundreds]) + len(nums_as_letters_dict[digit]))
    elif num_str[1] == "0":
        hundreds = int(num_str[0]) * 100
        digit = int(num_str[2])

        total_letters += (len(nums_as_letters_dict[hundreds]) + len(nums_as_letters_dict[digit]) + 3)
    elif num_str[1] == "1":
        hundreds = int(num_str[0]) * 100
        tens = int(num_str[1:])

        total_letters += (len(nums_as_letters_dict[hundreds]) + len(nums_as_letters_dict[tens]) + 3)
    else:
        hundreds = int(num_str[0]) * 100
        tens = int(num_str[1]) * 10
        digit = int(num_str[2])

        total_letters += (len(nums_as_letters_dict[hundreds]) + len(nums_as_letters_dict[tens]) + len(nums_as_letters_dict[digit]) + 3)

total_letters += len("onethousand")

print(f"\nThe total number of letters used is: {total_letters}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
