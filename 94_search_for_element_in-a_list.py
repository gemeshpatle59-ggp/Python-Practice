#  Search for an element in a list

def search_element(l1 , k):

    for i in range(len(l1)):

        if l1[i] == k:
            print(f"{k} is present in a list at index {i}")


search_element([1,2,3,4,5] , 5)
