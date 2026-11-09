#  Remove spaces from a string

def remove_space(str):

    new_str = ""

    for i in str:
        if i == " ":
            continue
        else:
            new_str += i

    return new_str


print(remove_space("gemesh patle"))