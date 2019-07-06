m = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4]

# Hãy tìm cách loại những phần tử xuất hiện lặp lại. m' = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12]

m2 = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4]
for i in range(1, 12):
    for j in range(0, i):
        if m[i] == m[j]:
            print(i)

#m2.pop(m2[10])

print(m2)