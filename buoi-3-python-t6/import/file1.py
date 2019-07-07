print(f"__name__ = {__name__}, __file__ = {__file__}")
avar = 10  # biến global

if __name__ == "__main__":
    print("File1 is being run directly")
else:
    # Nếu được file khác import đoạn này sẽ chạy
    print("File1 is being imported")
