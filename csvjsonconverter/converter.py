import csv
import json
import io

def convert_csv_to_json(csv_file, json_file):
    # Check if csv_file is a string (CSV data) or a file path
    if isinstance(csv_file, str) and '\n' in csv_file:  # It's a string, not a file path
        csv_file = io.StringIO(csv_file)  # Convert string to file-like object
    
    # Read the CSV file or string data
    with open(csv_file, mode="r", encoding="utf-8") if isinstance(csv_file, str) else csv_file as file:
        reader = csv.DictReader(file)
        data = []
        
        # Process each row to respect original data types
        for row in reader:
            for key, value in row.items():
                # Try to convert the value to a numeric type (int or float), leave it as string if it fails
                try:
                    if '.' in value:
                        row[key] = float(value)
                    else:
                        row[key] = int(value)
                except ValueError:
                    row[key] = value  # Keep it as string if conversion fails
            data.append(row)
    
    # Write the JSON output to the specified file
    with open(json_file, mode="w", encoding="utf-8") as jsonf:
        json.dump(data, jsonf, indent=4)
