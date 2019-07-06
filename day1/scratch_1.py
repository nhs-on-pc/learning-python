def chap2mang(array1, array2):
    array3 = array1 + array2
    array3.sort(key=int, reverse=False)
    print(array3)


a = [1, 2, 3, 8, 10]
b = [7, 9, 10]
chap2mang(a, b)
