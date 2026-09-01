#  Convert uppercase character to lowercase

n = input("Enter the character only.: ")

def lowercase_to_uppercase(n):

    for char in n:
        lower = ord(char)-64
        print(f"lower_case character of {char} is {chr(96+lower)}")

lowercase_to_uppercase(n)    