from time import time

start = time()

powSet = set()
for a in range(2,101):
    for b in range(2,101):
        powSet.add(a**b)
powSet = list(powSet)
print(len(powSet))

end = time()

print(f"\n{end-start} seconds")
