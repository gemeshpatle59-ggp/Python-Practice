#  Find sum of all elements in a list


def sum_of_list_element(l1):

    total = 0

    for x in l1:
        total += x

    return total

nums = [1,2,3,4,5]
print(sum_of_list_element(nums))