# Count_even_and_odd_numbers_in_a_list

def even_odd_in_list(l1):

    even = []
    odd = []

    for x in l1:
        if x % 2 == 0:
            even.append(x)

        else:
            odd.append(x)

    return f"even = {even} \nodd = {odd}"


nums = [1,2,3,4,5,6,7,8,9,10]
print(even_odd_in_list(nums))