#  Convert a string to title case

def title_string(str):

    result = ""
    new_word = True


    for i in str:
        if i == " ":
            result += i
            new_word = True

        elif new_word:
            result += i.upper()
            new_word = False

        else:
            result += i.lower()

    return result

print(title_string("gemesh patle"))
