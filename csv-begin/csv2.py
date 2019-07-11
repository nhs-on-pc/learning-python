import csv

with open("movies.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Columns names are \t {row[0]}, {row[1]}, {row[2]}")
            line_count += 1
        elif line_count < 1000:
            print(f"{'-'.join(row)}")
            line_count += 1
    print(f"Data has {line_count} rows")