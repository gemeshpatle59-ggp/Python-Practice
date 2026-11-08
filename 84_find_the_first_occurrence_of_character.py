#  Find the first occurrence of a character

def first_occurrence():

    string = input("Enter a string: ")
    ch = input("Enter character to search: ")

    found = False

    for i in range(len(string)):

        if string[i] == ch:
            print("First occurrence at index:", i)
            found = True
            break

    if not found:
        print("Character not found")


if __name__ == "__main__":
    first_occurrence()