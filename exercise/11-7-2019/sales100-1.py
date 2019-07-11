import csv

with open('sales100.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv
    region_set = set()

    for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
        region = row[0].split(',')
        region_set |= set(region)

    list_region = list(region_set)
    print(sorted(list_region))
