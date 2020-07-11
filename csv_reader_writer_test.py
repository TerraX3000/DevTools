import csv
import json

with open('Template for FET-Generated Timetable - Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["firstName"]} works in the {row["courseName"]} department, and was born in {row["days"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
print(type(csv_reader))
prettySchedule = json.dumps(csv_reader, indent=4, separators=("", " = "))
