m = [3, 2, 1, 2, 3, 4, 6, 8, 7, 4, 5, 10, 11, 12, 15, 16, 17, 18, 22, 18, 17]  # 21

'''
b1: so sánh giữa các vị trí i và i+1 trong mảng m. Nếu tìm ra vị trí nào nhỏ hơn, đếm số phần tử trong dãy tăng đó 
và ngắt nhỏ 
b2: xem bộ đếm nào có kết quả cao nhất, in ra số đó và in ra mảng 
'''

count = 0
max_count = 0
n = []
print(len(m))

for i in range(0, len(m)-1):
    if m[i] < m[i+1]:
        n.append(m[i])
        count += 1
        if m[19] > m[20]:
            n.append(m[20])
    else:
        n.append('count = ' + str(count))
'''
for i in range(0, len(list)-1):
    if list[i+1] >= list[i]:
        ketqua.append(list[i+1])
        count += 1
        if i == len(list)-2:
            ketqua.append("count = " + str(count))
'''
print(n)
print(m[17])
print(m[18], m[19])
