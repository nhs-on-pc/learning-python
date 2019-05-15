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





