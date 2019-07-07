def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    # Traverse both array
    while i < n1 and j < n2:

        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    while i < n1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1

    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1

    return arr3

l1 = [1, 2, 5, 7, 9, 10, 14, 20, 100]
l2 = [6, 8, 15, 20, 21, 40]
from time import time
start = time()
l3 = mergeArrays(l1, l2, len(l1), len(l2))
delta = (time()-start)
print(delta * 100000000)

print(l3)