#  Find the largest number in a list

def largest_num(l1):

    largest = float("-inf")

    for x in l1:
        if x > largest:
            largest = x

    return largest


nums = [1,2,3,5,6,7,9,8,77,7,7,8,8,98]
print(largest_num(nums))