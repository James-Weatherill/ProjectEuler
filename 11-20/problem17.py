from num2words import num2words
from time import time

start = time()

count = 0
for i in range(1,1001):
    num = num2words(i, lang='en')
    num = num.replace(" ","").replace("-","")
    count += len(num)
    
end = time()

print(count)  
print(f"{end-start} seconds!")
