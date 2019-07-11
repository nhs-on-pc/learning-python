# Đối với từng item type, sau khi sắp xếp A-Z hãy tính tổng doanh thu Total Revenue

# Lấy ra từng item type, sort
# Lấy ra doanh thu, rồi tính tổng
# in ra
import csv

with open('sales100.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv
    result = dict()
    count = 0
    revenue = 0


