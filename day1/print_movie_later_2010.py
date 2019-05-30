import csv

with open('movies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            film = row[1]
            if film.endswith(" "):
                year = film[-6:-2]
            else:
                year = film[-5:-1]

            try: # Cần phải có try để bắt lỗi khi convert string sang int
                if int(year) >= 2010:
                    #print(f'{row[0]} - {row[1]} - {row[2]}.')
                    pass
            except ValueError:
                print(f"{line_count} - {film}")
                #pass



        line_count += 1
    print(f'Processed {line_count} lines.')