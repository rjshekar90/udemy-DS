
#Hard coding method
#Use default dict method here

def anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return  False

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for _ in count:
        if count[_] != 0:
            return  False

    return True



print anagram("clint eastwood", "old west action")

