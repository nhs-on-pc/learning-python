l1 = [1, 2, 5, 7, 9, 10, 14, 20, 100]
l2 = [6, 8, 15, 20, 21, 40]

# https://www.geeksforgeeks.org/merge-two-sorted-arrays/

def merge(l1, l2):
    i = 0
    j = 0
    k = 0
    len1 = len(l1)
    len2 = len(l2)

    l3 = [None] * (len1 + len2)
    while i < len1 and j < len2:
        num1 = l1[i]
        num2 = l2[j]
        if num1 < num2:
            l3[k] = num1
            i += 1
            k += 1
        elif num1 > num2:
            l3[k] = num2
            j += 1
            k += 1
        else:
            l3[k] = num1
            l3[k + 1] = num2
            i += 1
            j += 1
            k += 2

    # Đoạn code này viết tốt hơn. Trong vì nó đẩy phần copy phần còn lại ra hoặc vòng while số 1, program
    # ít không phải duyệt qua
    while i < len1:
        l3[k] = l1[i]
        k += 1
        i += 1

    while j < len2:
        l3[k] = l2[j]
        k += 1
        j += 1

    return l3

from time import time
start = time()
l3 = merge(l1, l2)
delta = (time()-start)
print(delta * 100000000)
print(l3)




'''
head1 |  head2 | smallernum | from  | l3
0     |  0     |  1         | l1    | 1
1     |  0     |  2         | l1    | 1, 2
2     |  0     |  5         | l1    | 1, 2, 5
3     |  0     |  6         | l2    | 1, 2, 5, 6
3     |  1     |  7         | l1    | 1, 2, 5, 6, 7
4     |  1     |  8         | l2    | 1, 2, 5, 6, 7, 8

'''

