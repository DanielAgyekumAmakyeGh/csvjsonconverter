import argparse
from csvjsonconverter.converter import convert_csv_to_json

def main():
    parser = argparse.ArgumentParser(description="Convert CSV data to JSON format.")
    
    # Add arguments for input CSV file (or string) and output JSON file
    parser.add_argument('csv_data', help="Path to the input CSV file or CSV data as string")
    parser.add_argument('json_file', help="Path to save the output JSON file")

    # Parse the arguments
    args = parser.parse_args()

    # Call the conversion function
    convert_csv_to_json(args.csv_data, args.json_file)
    print(f"Conversion complete! JSON data saved to {args.json_file}")

if __name__ == "__main__":
    main()
