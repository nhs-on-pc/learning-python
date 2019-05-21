import pandas as pd
# Nếu gặp lỗi ImportError: No module named 'xlrd' hãy pip install xlrd

sheet = pd.read_excel('DanhSach.xlsx', 'Sheet1')

# Danh sách các cột ~ (hàng đầu tiên)
#print(sheet.columns)

# Kích thước mảng dữ liệu
#print(sheet.shape)

#Lấy dữ liệu
#print(sheet.head())  # Có thể truyền số tự nhiên vào head()

# Thông kê tuổi
print('Min: ', sheet['Age'].min())
print('Max: ', sheet['Age'].max())
print('Sum: ', sheet['Age'].sum())

print("----- Short by Age ------")
print(sheet['Age'].sort_values())

print("----- Cell at row[1] of column['Xưng hô'] ------")
print(sheet['Xưng hô'][1])

print("----- column Age ---------")
print(sheet['Age'].values)

# Loop through data frame
for index, row in sheet.iterrows():
    print(f"{row[0]} - {row[1]} {row[2]} có tuổi là {row[4]}")

