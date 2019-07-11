import csv  # import thư viện csv

with open('movies.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # mở file csv, ngăn giữa các cột bằng dấu ,
    line_count = 0
    for row in csv_reader:  # for loop, quét từng dòng trong file
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')  # In tên các cột
            line_count += 1
        elif line_count < 100:
            print(f'\t{row[0]} - {row[1]} - {row[2]}.')  # in dữ liệu, các dòng có index và ngăn cách bởi dấu -
            line_count += 1

    '''for i in {row[2]}:
        if i == "Drama":
            print(i)
    '''

    print(f'Processed {line_count} lines.')  # đếm số dòng của dữ liệu
