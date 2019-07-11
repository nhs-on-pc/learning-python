'''
Hãy viết một hàm tham số đầu vào là một mảng các số tự nhiên trả về một mảng gồm các ký tự + hoặc - hay = mô tả
phần tử tiếp theo tăng hay giảm hay bằng so với phần tử trước đó

sign = "+" if A[i+1] > A[i] else "-" if A[i+1] < A[i] else "="
Ví dụ: m = [1, 4, 4, 2, 3, 6, 7, 8, 5, 5] def inc_or_dec(array):->[String]

Kết quả trả về sẽ là ['+', '=', '-', '+', '+', '+', '+', '-', '=']
'''
m = [4,1,1,1,2,3,4,5,6,7,6,5]


def inc_or_dec(m):

    result = []
    for i in range(len(m)):
        if i == len(m)-1:
            break
        else:
            if m[i] < m[i+1]:
                result.append('+')
            elif m[i] == m[i+1]:
                result.append('=')
            else:
                result.append('-')
    print(result)


inc_or_dec(m)

