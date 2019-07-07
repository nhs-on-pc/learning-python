def say_hello(name):
    # Hàm này khi import sẽ chạyw
    print(f"Hello {name}")


def main():
    # Hàm chính được gọi nếu greeting được người dùng chạy trực tiếp
    print("Execute when user executes greeting.py directly")


if __name__ == '__main__':
    # Chạy chế độ execute
    main()
