a = [3, 2, 1, 2, 3, 4, 6, 8, 7, 4, 5, 10, 11, 12, 15, 16, 17, 18, 22, 18, 17]  # 21
n = []


def increasing(m):
    count = 0
    max_count = 0

    if m[0] < m[1]:
        n.append(m[0])
        n.append(m[1])
        n.append('count=' + str(2))
    
    for i in range(0, len(m)-2):
        if m[i] > m[i+1]:
            if m[i+1] < m[i+2]:
                n.append(m[i+1])
                n.append(m[i+2])
                count += 2
            else:

                continue
        else:  # <
            if m[i+1] < m[i+2]:
                n.append(m[i+2])
                count += 1
            else:
                n.append('count=' + str(count))
                if max_count < count:
                    max_count = count
                count = 0
                continue
    print(n)

# in ket qua
    print(f"Cac mang tinh tien nhieu nhat co " + str(max_count) + " phan tu")

    for i in range(0, len(n)):
        if n[i] == "count=" + str(max_count):
            msg: str = str(n[i-max_count:i])

    print(f"Mang tang dan nhieu phan tu nhat la " + msg)


increasing(a)

