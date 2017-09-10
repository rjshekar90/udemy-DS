
from collections import defaultdict

def anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    count = defaultdict(int)

    for k in str1:
        count[k] += 1

    for k in str2:
        count[k] -= 1

    for i in count:
        if count[i] != 0:
            return False
    return True

print anagram("clint eastwood", "old westaction")
