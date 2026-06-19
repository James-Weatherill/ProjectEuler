import os
from time import time

########################################

start_time = time()

########################################

def name_calc(name):
    cur_sum = 0

    for letter in name:
        cur_sum += letters.index(letter) + 1

    return cur_sum

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
file_path = os.path.join(assets_path, "0022_data.txt")

with open(file_path, "r+") as file:
    names_list = file.read().strip().split("\",\"")
    names_list[0] = names_list[0][1:]; names_list[-1] = names_list[-1][:-1]
    names_list.sort()

score = 0

for idx in range(len(names_list)):
    score += ((idx + 1) * (name_calc(names_list[idx])))

print(f"\nThe total score of the names is: {score}")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
