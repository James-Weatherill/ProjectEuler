num = 0
while True:
    found = False
    counter = 0
    num += 1
    numOrder = "".join(sorted(str(num)))
    for i in range(2,7):
        if numOrder!="".join(sorted(str(num*i))):
            break
        if i==6:
            found = True
            break
    if found:
        break
print(num)
            
