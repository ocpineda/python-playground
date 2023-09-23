import csv
import json

csv_file = 'convert-me.csv'
json_file = 'output.json'

data = []

with open(csv_file, mode = 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

with open(json_file, mode='w') as json_file:
    json.dump(data, json_file, indent=4)