import csv
import json

def convert_csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"JSON file saved: {json_file}")
 
