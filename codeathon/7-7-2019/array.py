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
m2 = []
for i in range(0, len(m)):
    for j in range(0, i-1):
        if m[i] != m[j]:
            m2 = m2.append(m[i])
print(m2)