#  Find average of list elements

def average_of_list_element(l1):

    average = 0
    n = len(l1)

    for x in l1:
        average += x

    average = average/n

    return average

nums = [1,2,3,4,5,6,7]

print(average_of_list_element(nums))