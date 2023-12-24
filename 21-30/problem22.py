from string import ascii_uppercase
from time import time

start = time()
total = 0

FILE = open("assets/0022_names.txt", "r+")
file = str(FILE.readlines())
file = file.replace(r"\n", '').replace('[', '').replace("', '", "").replace("'", "").replace('"', "")
file = file.split(",")
file[-1] = "ALONSO"
file = sorted(file)

for i in file:
    nameTot = 0
    for j in i:
        nameTot += ascii_uppercase.index(j)+1
    total += nameTot*(file.index(i)+1)
    
print(total)
end = time()
print((end-start), "seconds")
