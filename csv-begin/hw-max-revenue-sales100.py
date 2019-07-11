import csv

with open('sales100.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv
    region_set = set()

    for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
        region = row[0].split(',')
        region_set |= set(region)

    list_region = list(region_set)
    print(list_region)



'''
genres = row[2].split('|') genre_set |= set(genres) line_count += 1
 listphim = list(genre_set) print(listphim) print(f'Processed {line_count} lines.')
'''