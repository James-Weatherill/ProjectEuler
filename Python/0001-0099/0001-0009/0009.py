from time import time
from math import sqrt

########################################

start_time = time()

########################################

for a in range(1, 1001):
    for b in range(a + 1, 1001):
        found = False

        c = sqrt(a**2 + b**2)

        if (c % 1 == 0) and (a + b + int(c) == 1000):
            c = int(c)
            found = True
            break
    if found:
        break

print(f"""\nIf... a = {a}, b = {b}, and c = {c}, then...
a^(2) + b^(2) = {a**2} + {b**2} = {c**2} = c^(2), and...
a + b + c = {a} + {b} + {c} = {a + b + c}, therefore...
a * b * c = {a} * {b} * {c} = {a * b * c}""")

########################################

finish_time = time()

print(f"\nThe code took: {finish_time - start_time} seconds to run!\n")
