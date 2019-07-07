# Demo khác biệt giữa chạy trực tiếp file python VS gọi (import) file python

Nếu chạy file python thì biến môi trường __name__ == 



Sử dụng cú pháp ```from util.add import add```

## Thí nghiệm 1

```bash
python3 test_greeting.py
```
Bạn sẽ thấy test_greeting.py gọi hàm say_hello từ greeting.py và add từ file add.py trong thư mục util.
Để import file trong folder sẽ phải dùng cú pháp này ```from util.add import add```

Cấu hình PyCharm > Preferences > Project Structure > Chọn thư mục import_function như là Source

## Thí nghiệm 2

Có 2 file: file1.py và file2.py
Hãy chạy thử ```python3 file1.py``` so sánh với ```python3 file2.py```

Giải thích ý nghĩa ```if __name__ == "__main__"```

file2.py có lệnh import file1. Kết quả chạy sẽ như sau
```bash
File1 __name__ = file1
File1 is being imported
File2 __name__ = __main__
File2 is being run directly
```

