'''
Bài 4

Cho một mảng gồm n số tự nhiên, hãy tự viết hàm sắp xếp từ thấp lên cao, và ngược laị trả về một mảng mới.
Không cần tối ưu tốc độ, chỉ cần hàm chạy được và chạy đúnng

a = [2, 1, 5, 4, 7, 8]
sort(input: a, ascending: true)
[1, 2, 4, 5, 7, 8]
sort(input: a, ascending: true)
[8, 7, 5, 4, 2, 1]
'''

n = int(input("Nhap so chu so trong day: "))
lst = []
for i in range(0, n):
    ele = int(input("Moi nhap day so: "))
    lst.append(ele)
print("Day so da nhap: ", lst)
ascending_lst = sorted(lst, reverse= 0)
print("Day tang: ", ascending_lst)
decending_lst = sorted(lst, reverse= 1)
print("Day giam: ", decending_lst)
