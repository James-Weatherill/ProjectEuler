from time import time

########################################

start_time = time()

########################################

ans = 0

months1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
for year in range(1901, 2001):
    if (not year % 4 == 0) or (year % 4 == 0 and not year % 400 == 0):
        for month in months1:
            if day % 7 == 0:
                ans += 1
            day += month
    else:
        for month in months2:
            if day % 7 == 0:
                ans += 1
            day += month

print(f"""\nBetween 01/01/1901 and 31/12/2000, there are {ans} Sundays
that fall on the first of the month!""")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
