# tích dãy số từ 1 đến n
n = 5
s = n
while n > 0:
    s = s * (n - 1)
    n -= 1
    if n == 1:
        print(s)
        break

