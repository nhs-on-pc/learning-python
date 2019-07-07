from time import time
l1 = [1, 2, 5, 7, 9, 10, 14, 20, 100]
l2 = [6, 8, 15, 20, 21, 40]
start = time()
l3 = l1 + l2
l3.sort()
delta = (time()-start)
print(delta * 100000000)
print(l3)
