#  Remove duplicate elements from a list

def remove_duplicate(l1):

    duplicate = {}

    for x in l1:

        if x in duplicate:
            duplicate[x] += 1

        else:
            duplicate[x] = 1

    new_list = []
    for i in duplicate:
        if duplicate[i] == 1:
            new_list.append(i)

    return new_list

print(remove_duplicate([1,2,3,1,2,3,4,5,6,7,4,5,8,9,5,9,10]))