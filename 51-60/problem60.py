#! /opt/homebrew/bin/python3

from time import time
from sympy import isprime
from copy import deepcopy as copy

startTime = time()

########################################

file = open("assets/0060_primeList.txt", "r")
fileReadStr = (str(file.readlines())[2:-4]).split(",")
fixedList = [num for num in fileReadStr]

########################################

#for sequence 3, 7, 109, 673, the fifth number is: 129,976,621. The sum of this is: 129,977,413
#for sequence 3, 7, 109, 91,159, the fifth number is: 2,622,679. The sum of this is: 2,713,957
#for sequence 3, 7, 19,237, 83,023, the fifth number is: 343,771. The sum of this is: 446,041
#for sequence 3, 37, 67, 5,923, the fifth number is: 194,119. The sum of this is: 200,149
#for sequence 3, 5,323, 10,357, 29,587, the fifth number is: 31,231. The sum of this is: 76,501
#for sequence 13, 5,197, 5,701, 6,733, the fifth number is: 8,389. The sum of this is: 26,033

thePrimes = [13, 5197, 5701, 6733, 8389]

lowestSoFar = 26_033

for i in range(len(fixedList[0:-4])):

    for j in range(i+1, len(fixedList[:-3])):

        iAndJ = int(fixedList[i]+fixedList[j])
        jAndI = int(fixedList[j]+fixedList[i])

        iToJSum = int(fixedList[i])+int(fixedList[j])

        if iToJSum >= 26_033:
            break

        if isprime(iAndJ) and isprime(jAndI):

            for k in range(i+2, len(fixedList[:-2])):

                iAndK = int(fixedList[i]+fixedList[k])
                kAndI = int(fixedList[k]+fixedList[i])
                jAndK = int(fixedList[j]+fixedList[k])
                kAndJ = int(fixedList[k]+fixedList[j])

                iToKSum = iToJSum + int(fixedList[k])

                if iToKSum >= 26_033:
                    break

                if isprime(iAndK) and isprime(kAndI) and isprime(jAndK) and isprime(kAndJ):

                    for l in range(i+3, len(fixedList[:-1])):

                        iAndL = int(fixedList[i]+fixedList[l])
                        lAndI = int(fixedList[l]+fixedList[i])
                        jAndL = int(fixedList[j]+fixedList[l])
                        lAndJ = int(fixedList[l]+fixedList[j])
                        kAndL = int(fixedList[k]+fixedList[l])
                        lAndK = int(fixedList[l]+fixedList[k])

                        iToLSum = iToKSum + int(fixedList[l])

                        if iToLSum >= 26_033:
                            break

                        if isprime(iAndL) and isprime(lAndI) and isprime(jAndL) and isprime(lAndJ) and isprime(kAndL) and isprime(lAndK):

                            for m in range(i+4, len(fixedList)):

                                iAndM = int(fixedList[i]+fixedList[m])
                                mAndI = int(fixedList[m]+fixedList[i])
                                jAndM = int(fixedList[j]+fixedList[m])
                                mAndJ = int(fixedList[m]+fixedList[j])
                                kAndM = int(fixedList[k]+fixedList[m])
                                mAndK = int(fixedList[m]+fixedList[k])
                                lAndM = int(fixedList[l]+fixedList[m])
                                mAndL = int(fixedList[m]+fixedList[l])

                                iToMSum = iToLSum + int(fixedList[m])

                                if iToMSum >= 26_033:
                                    break

                                if isprime(iAndM) and isprime(mAndI) and isprime(jAndM) and isprime(mAndJ) and isprime(kAndM) and isprime(mAndK) and isprime(lAndM) and isprime(mAndL):
                                    if iToMSum < lowestSoFar:
                                        lowestSoFar = copy(iToMSum)
                                        thePrimes = [fixedList[i], fixedList[j], fixedList[k], fixedList[l], fixedList[m]]

print(lowestSoFar)
print(thePrimes)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

