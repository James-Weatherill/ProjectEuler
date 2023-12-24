from time import time

start = time()

length = 2

botR = [3]
botL = [5]
topL = [7]
topR = [1,9]

while topR[-1]!=1002001:
    length += 2
    botR.append(topR[-1]+length)
    botL.append(botR[-1]+length)
    topL.append(botL[-1]+length)
    topR.append(topL[-1]+length)

print(sum(topL+topR+botL+botR))

end = time()

print(f"\n{end-start} seconds!")

