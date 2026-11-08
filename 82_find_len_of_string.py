# Find length of a string without len


def length_string(s):
    length = 0

    for i in s:
        length += 1

    return length

print(length_string("bittu"))