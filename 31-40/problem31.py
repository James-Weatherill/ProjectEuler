from time import time

start = time()

combos = 0
for g in range(3): #£1
    for f in range(5): #50p
        for e in range(11): #20p
            for d in range(21): #10p
                for c in range(41): #5p
                    for b in range(101): #2p
                        for a in range(201): #1p
                            num = (1*a)+(2*b)+(5*c)+(10*d)+(20*e)+(50*f)+(g*100)
                            if num>200:
                                break
                            elif num==200:
                                combos += 1                             
end = time()

print(combos+1)
print(f"{end-start} seconds!")
                            
