l1 = [1, 2, 5, 7, 9, 10, 14, 20, 100]
l2 = [6, 8, 15, 20, 21, 40]


from time import time
start = time()
for num in l2:
    if num < l1[0]:
        l1.insert(0, num)
    elif num > l1[len(l1) - 1]:
        l1.append(num)
    else:
        left = 0
        right = len(l1) - 1
        while 1:
            mid = (left + right) // 2
            if num < l1[mid]:
                right = mid
                continue
            elif l1[mid] <= num <= l1[mid + 1]:
                l1.insert(mid + 1, num)
                break
            else:
                left = mid
                continue

delta = (time()-start)
print(delta * 100000000)
print(l1)

'''
num = 8
mid = 4
[1, 2, 5, 7, 9, 10, 14, 20, 100]

num | left | right | mid | l1[mid]
8   | 0    | 8     | 4   | 9       right -> mid = 4
8   | 0    | 4     | 2   | 5       left --> mid = 2
8   | 2    | 4     | 3   | 7
'''