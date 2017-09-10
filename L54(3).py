
#Array Pair sum

def pair_sum(arr, k):

    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:

        target = k - num

        if target in seen:
            seen.add(num)

        else:
            output.add((min(target, num), max(target, num)))

    print "\n".join(map(str, list(output)))

pair_sum([2,2,1,3], 4)