# Count frequency of elements in a list

def frequency(l1):

    freq = {}

    for x in l1:
        if x in freq:
            freq[x] += 1

        else:
            freq[x] = 1

    for x in freq:
        print(f"item = {x} \nfrequency = {freq[x]} \n ")

list1 = [1,1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7,7,8,9,0,0,0]
frequency(list1)