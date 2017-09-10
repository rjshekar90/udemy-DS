
from collections import defaultdict

def finder(arr1, arr2):

    d = defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print finder([1,2,3,4], [2,3,4])




