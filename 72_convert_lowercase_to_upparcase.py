# Convert lowercase character to uppercase

n = input("Enter the character only.: ")

def lowercase_to_uppercase(n):

    for char in n:
        uppar = ord(char)-96
        print(f"Uppar_case character of {char} is {chr(64+uppar)}")

lowercase_to_uppercase(n)        
