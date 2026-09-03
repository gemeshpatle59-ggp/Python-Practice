# Check whether a character is an alphabet, digit, or special character

def check_character():
        n = input("ENTER THE CHArACTER HERE.: ")

        if 97 <= ord(n[0]) <= 122 or 65 <= ord(n[0]) <= 90:
            print("The character is Alphabate")

        elif 48 <= ord(n[0]) <= 57:
            print("The Character is Integer")

        else:
            print("The Character is a Symbol")     

check_character()            