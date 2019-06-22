import numpy

a = [1, 2, 1, 2, 1, 3, 1, 4]
b = sorted(a)
print(b)
n1 = n2 = n3 = n4 = 0

for i in b:
    if i == 1:
        n1 += 1
    elif i == 2:
        n2 += 1
    elif i == 3:
        n3 += 1
    else:
        n4 += 1
myDict = {1: n1, 2: n2, 3: n3, 4: n4}
n = (n1, n2, n3, n4)
c = numpy.amax(n)

if c == n1:
    print(f'1 xuat hien {c} lan')



