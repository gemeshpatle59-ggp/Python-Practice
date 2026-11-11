# Sort a list without using sort()


def bubble_sort(l1):
    n = len(l1)

    for x in range(n):
        is_swaped = False
        for y in range(n-x-1):
            if l1[y] > l1[y+1]:
                l1[y] , l1[y+1] = l1[y+1] , l1[y]
                is_swaped = True

        if not is_swaped:
            break

    return l1

print(bubble_sort([9,8,7,6,5,4,3,2,1]))