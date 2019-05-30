import csv

with open('movies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    genre_set = set()
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            genres = row[2].split('|')
            genre_set |= set(genres)
            line_count += 1
    print(genre_set)
    print(f'Processed {line_count} lines.')