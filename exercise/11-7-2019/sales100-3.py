import csv

with open('sales100.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    revenue = 0
    line_count = 0
    for row in csv_reader:
        if line_count > 0 and row[2] == "Baby Food":
            revenue = revenue + float(row[11])
        line_count += 1

    print(revenue)

# lọc item type baby food

# lấy revenue của baby food

# cộng revenue của baby food
