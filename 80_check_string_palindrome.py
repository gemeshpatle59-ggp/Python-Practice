#  Check whether a string is a palindrome

def check_palindrome(s):

    new_s = ""

    for i in range(len(s)-1 , -1, -1):
        new_s += s[i]

    return s == new_s

print(check_palindrome("gemesh"))