
import csv

with open('./day2/data/names.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    with open('./day2/data/new_names.csv', 'w') as newfile:
        fnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(newfile, fieldnames=fnames, delimiter=',')

        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

        print('New file created')

print('New csv exported')