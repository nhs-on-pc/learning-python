import xlrd

wb = xlrd.open_workbook("DanhSach.xlsx")
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Extracting number of rows
print(sheet.nrows)

# Extracting number of columns
print(sheet.ncols)

# Đọc dòng 0 ~ column header
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

# In ra dòng số 3
print(sheet.row_values(2))
print(sheet.row_values(2)[1])  #Lấy ra Họ Đệm

print(sheet.col_values(1))

print(sheet.col_values(4))