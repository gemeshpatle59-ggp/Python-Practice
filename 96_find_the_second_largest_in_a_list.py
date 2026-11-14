#  Find second largest number in a list

def second_largest_element(l1):

    x = float("-inf")
    y = 0

    for i in l1:
        if i > x:
            y = x
            x = i



    return y

print(second_largest_element([1,2,3,4,5,4,8,9,7,6]))