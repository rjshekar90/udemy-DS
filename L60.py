# Reverse the words in a list

def rev_words(s):

    words = []
    length = len(s)
    spaces = [" "]

    i = 0

    while i < length:
        if s[i] not in spaces:

            wordstart = i

            while i < length and s[i] not in spaces:

                i += 1
            words.append(s[wordstart:i])

        i += 1

    return " ".join(reversed(words))

print rev_words('   Hello John    how are you   ')

**************************************************************
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
