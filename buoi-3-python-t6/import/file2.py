import file1  # sử dụng file1
# file1 sẽ được chạy trước tiên


def main():
    print("File2 is being run directly")
    print(f"File2 __name__ = {__name__}" )
    print(file1.avar)
    file1.avar = 12
    print(file1.avar)


if __name__ == "__main__":   # Nếu được chạy từ chính file này
    main()  # Thì gọi hàm main
else:
    # Còn không file này được import
    print("File2 is being imported")

