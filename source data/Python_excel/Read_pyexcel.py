# Cài đặt pip install pyexcel, pyexcel-xls
# pyexcel khá dễ dùng nhưng không hỗ trợ Formula

import pyexcel as p
book = p.get_book(file_name="DanhSach.xlsx")
#print(book.Sheet1)

sheet = p.get_sheet(file_name="DanhSach.xlsx")
sheet.name_columns_by_row(0)  # Bỏ đi hàng đầu tiên chưa tên cột

# In ra 2 cell trên mỗi dòng dữ liệu
for row in sheet:
    print(row[0], row[1])

print(sheet.column[4])