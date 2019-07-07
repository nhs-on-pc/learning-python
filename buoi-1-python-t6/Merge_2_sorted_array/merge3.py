l1 = [1, 2, 5, 7, 9, 10, 14, 20, 100]
l2 = [6, 8, 15, 20, 21, 40]

# https://www.geeksforgeeks.org/merge-two-sorted-arrays/


def merge(l1, l2):
    head1 = 0
    head2 = 0
    l3 = []
    while True:
        num1 = l1[head1]
        num2 = l2[head2]
        if num1 < num2:
            l3.append(num1)
            head1 += 1
        elif num1 > num2:
            l3.append(num2)
            head2 += 1
        else:
            l3.append(num1)
            l3.append(num2)
            head1 += 1
            head2 += 1

        if head1 == len(l1):
            l3.extend(l2[head2:])
            break

        if head2 == len(l2):
            l3.extend(l1[head1:])
            break
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

