import csv

with open('sales100.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv
    item_type_set = set()
    count = 0
    for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
        if count > 0:
            item_type_set.add(row[2])
        count += 1

    print(sorted(item_type_set))