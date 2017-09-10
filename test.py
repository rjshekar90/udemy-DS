
def cont_sum(arr):

    if len(arr) == 0:
        return

    max_sum = curr_sum = arr[0]

    for num in arr[1:]:

        curr_sum = max(curr_sum+num, num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

print cont_sum([1,2,-1,3,4,10,10,-10,-1])