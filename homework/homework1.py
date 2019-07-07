# Phương trình bậc 2
def ptb2(a: float, b: float, c: float):
    if a <= 0 and (b, c) < 0:
        print("Nhap lai a, b, c")
    else:
        delta = b*b - 4*a*c

        if delta < 0:
            #print(-delta**(1/2))
            x1 = complex(-b/(2*a), -(-delta**(1/2))/(2*a))
            x2 = complex(-b/(2*a), +(-delta**(1/2))/(2*a))
            print("Phuong trinh co hai nghiem phuc phan biet: ", x1, x2)

        elif delta == 0:
            x = round(-b/(2*a), 3)
            print("Nghiem kep cua phuong trinh la: ", x)
        else:
            x3 = round((-b - delta**(1/2))/(2*a), 3)
            x4 = round((-b + delta**(1/2))/(2*a), 3)
            print("Phuong trinh co hai nghiem: ", x3, x4)

ptb2(1, 3, -2)

# Số nguyên tố
i = int(input("Nhập i: "))
for i in range(4, i + 1):
    isPrime = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            isPrime = False
            break
        if i % j != 0:
            continue
    if isPrime is True:
        print(i)

# trò chơi tìm số trong dãy

import random
x = random.randint(0, 10)

for n in range(0, 11):
    n = int(input("Mời nhập số bạn đoán: "))
    if n < x:
        print("Nhỏ hơn")
        continue
    elif n > x:
        print("Lớn hơn")
        continue
    else:
        print("Chính xác")
        break

# Truyền vào dãy tham số int (variadic) hãy trả về số lớn nhất nhì

a = [1, 2, 3, 9, 6, 2, 5, 10, 15]
solon = a[0]
for i in range(1, len(a)):
    if solon < a[i]:
        solon = a[i]
print(solon)

sonho = a[0]
for i in range(1, len(a)):
    if sonho > a[i]:
        sonho = a[i]
print(sonho)
