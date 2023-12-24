import numpy as np

goodNum = [0]

nums1 = np.arange(1,1000)
nums2 = np.arange(1,1000)

for i in nums1:
    for j in nums2:
        multi = i*j
        if str(multi)==(str(multi))[::-1] and multi>goodNum[0]:
            goodNum = []
            goodNum.append(multi)
            
print(goodNum)
        
