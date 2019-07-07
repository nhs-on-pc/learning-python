from greeting import say_hello  # Có thể thay say_hello bằng *
from util.math import *  # Có thể thay add bằng *


def main():
    # Hàm chính được gọi nếu test_greeting được người dùng chạy
    say_hello("Cuong")
    print(add(10, 2))
    print(minus(10, 2))


if __name__ == '__main__':
    main()
