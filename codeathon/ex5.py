'''
Bài 5

Nhập vào số tự nhiên 2 =< m, n < 8, hãy dựng thành một ma trận có m hàng và n cột, các phần tử là
số tự nhiên được sinh ngẫu nhiên (random) < 10, in ra màn hình ma trận này

$ Nhập m
$ 2
$ Nhập n
$ 3
2  3  4
1  5  8
'''

m = int(input("Moi nhap m >= 2: "))
n = int(input("Moi nhap n < 8: "))
while m < 2 or n > 8:
    print("Nhap sai, moi nhap lai: ")
    m = int(input("Moi nhap m >= 2: "))
    n = int(input("Moi nhap n < 8: "))
    continue

if m >= 2 and n < 8:
    print(m, n)





