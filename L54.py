
#array pair sum
#See other soln. this is o(nlogn).

def pairSum(arr, k):
    if len(arr) < 2:
        pass

    arr.sort()
    left, right = (0, len(arr) - 1)

    while left < right:
        currentSum = arr[left] + arr[right]

        if currentSum == k:
            print arr[left], arr[right]

        elif currentSum < k:
            left += 1

        else:
            right -= 1



print pairSum([1,3,2,2], 4)