#  Check whether a character is a vowel or consonant

n = input("ENTER THE CHARACTER HERE.: ")


def check_vowel_consonant(n):
    m = ["a","e","i","o","u"]
    for chr in (m):
        if n.lower() == chr:
            print(f"{n} is a vowel")
            return
        else:
            print(f"{n} is a consonant.")
            break

check_vowel_consonant(n)


        