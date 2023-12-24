import numpy as np

hundSqdSum = np.arange(1,101)
hundSumSqd = np.arange(1,101)

total = 0

for i in hundSqdSum:
    total += i**2

hundSumSqd = (sum(hundSumSqd))**2

diff = hundSumSqd-total

print(diff)
