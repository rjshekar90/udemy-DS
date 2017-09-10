
#Using XOR Operations
# http://www.ardendertat.com/2011/09/27/programming-interview-questions-4-find-missing-element/

def missingNumber(arr1, arr2):

    result = 0

    for num in arr1 + arr2:
        result^=num

    return result

print missingNumber([1,2,3,4], [1,2,3])