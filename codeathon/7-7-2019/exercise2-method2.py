a = [3, 2, 1, 2, 3, 4, 6, 8, 7, 4, 5, 10, 11, 12, 15, 16, 17, 18, 22, 18, 17]
b = []
def increasing(a):
    count = 0
    for i in range(1, len(a)):
        if a[i-1] < a[i]:
            b.append(a[i])

