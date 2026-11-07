# Count consonants in a string

def count_consonants(s):

    n = {"a" , "e" , "i" , "o" , "u"}
    consonants = 0

    for i in s:
        if i not in n:
            consonants += 1

    return consonants

print(count_consonants("gemesh"))