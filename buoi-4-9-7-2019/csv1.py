import csv

with open('movies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} - {row[1]} - {row[2]}.')
            line_count += 1
    for i in {row[2]}:
        if i == "Drama":
            print(i)
    print(f'Processed {line_count} lines.')
