##method 1:
list = [3, 2, 1, 2, 3, 4, 6, 8, 7, 4, 5, 10, 11, 12, 15, 16, 17, 18, 22, 18, 17]  # 21

ketqua = [list[0]]
count = 1
count_max = 1

#b1:loop qua tung gia tri trong mang. append list[i] vao ketqua
#b2:check list[i+1] co lon hon list[i] hay ko. Neu co thi append list[i+1] vao ketqua
#neu ko thi ghi so luong phan tu vao ben canh, sau do check doan tiep theo trong list
for i in range(0, len(list)-1):
    if list[i+1] >= list[i]:
        ketqua.append(list[i+1])
        count += 1
        if i == len(list)-2:
            ketqua.append("count = " + str(count))

    if list[i+1] < list[i]:
        ketqua.append("count = " + str(count))
        if count_max < count:
            count_max = count
        count = 1
        ketqua.append(list[i+1])
print(ketqua)

#in ket qua:
print("Các mảng tịnh tiến nhiều nhất có "+str(count_max)+" phần tử")
print("Các mảng này là: ")
for i in range(0, len(ketqua)):
    if ketqua[i] == "count = "+str(count_max):
        msg = str(ketqua[i-count_max:i])
        print(msg)