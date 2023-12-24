from math import factorial as fact

hunFact = list(str(fact(100)))
for i in range(len(hunFact)):
    hunFact[i] = int(hunFact[i])
    
print(sum(hunFact))
