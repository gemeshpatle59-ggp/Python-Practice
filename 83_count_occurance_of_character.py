#  Count occurrence of a characte


def occurrence_character(s):

    occerrence = {}

    for i in s:
        if i in occerrence:
            occerrence[i] += 1

        else:
            occerrence[i] = 1

    return occerrence

print(occurrence_character("gghhttrrggd"))