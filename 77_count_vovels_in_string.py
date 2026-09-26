"""
Count vowels in a string

"""

def count_vovels(s,):

    vovels = {"a" , "e" , "i" , "o" , "u"}
    count_vovel = 0

    for i in s:
        if i in vovels:
            count_vovel += 1
    return count_vovel

print(count_vovels("gemesh ananatkumar patle "))