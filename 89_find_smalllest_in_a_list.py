#  Find the smallest number in a list

def smallest_in_list(l1):

    smallest = float("inf")

    for x in l1:
        if x < smallest:
            smallest = x

    return smallest

nums = [1,2,3,4,5,6]
print(smallest_in_list(nums))