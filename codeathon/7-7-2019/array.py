m = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4]

# Hãy tính tổng các phần tử thuộc m
    # Cách 1: dùng hàm sum
a = sum(m)
print(a)
    # Cách 2: dùng vòng lặp for
b = m[0]
for i in range(1, len(m)):
    b = b + m[i]
print(b)
    # Cách 3: dùng array python slice
sum(m[0:])
print(sum(m[0:]))

# Tìm số lớn nhất trong m
    #Cách 1: dùng hàm có sẵn
print(max(m))
    #Cách 2: tự viết
solon = m[0]
for i in range(1, len(m)):
    if solon < m[i]:
        solon = m[i]
print(solon)

# Tính trung bình cộng các phần tử trong m
tbc = b / len(m)
print(tbc)

# In mảng trên theo thứ tự nghịch đảo 4, 2, 12, 9, 5, 8, 7, 6, 3, 2, 4, 1
print(m [::-1])

# Hãy tìm cách loại những phần tử xuất hiện lặp lại. m' = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12]
m = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4]
m2 = []
a = []

for i in range(1, 12):
    for j in range(0, i):
        if m[i] == m[j]:
            a.append(i)
print(a)
for i in range(0, 12):
    if i in a:
        break
    else:
        m2.append(m[i])

print(m2)

# In ra khoảng cách giữa các phần tử: D[i] = m[i+1] - m[i] D = [3, -2, 1, 3, 1, 1, -3, 4, 3, -10, 2]
m = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4]
d = []
for i in range(0, 11):
    d.append(m[i+1]-m[i])
print(d)

# trò chơi tìm số trong dãy


def guessnumber(n: int):
    import random
    x = random.randint(0, n)

    for i in range(0, n+1):
        i = int(input("Mời nhập số bạn đoán: "))
        if i < x:
            print("Nhỏ hơn")
            continue
        elif i > x:
            print("Lớn hơn")
            continue
        else:
            print("Chính xác")
            break


guessnumber(10)