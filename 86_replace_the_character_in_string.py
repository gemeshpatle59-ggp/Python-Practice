#  Replace a character in a string

def replace_character(str , pev_chr , new_chr):

    new_str = ""

    for i in str:
        if i == pev_chr:
            new_str += new_chr

        else:
            new_str += i

    return new_str

print(replace_character("gemesh" ,"g" , "j"))