import unittest
import json
import tempfile
from converter import convert_csv_to_json

class TestConverter(unittest.TestCase):

    def test_convert_csv_data_string_to_json(self):
        # CSV string to be converted
        input_csv_string = 'name,age\nJohn,30\nJane,25.5'

        # Create temporary JSON file for output
        with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8') as temp_json_file:
            temp_json_file_path = temp_json_file.name

        # Call the function with the CSV string and the temporary JSON file path
        convert_csv_to_json(input_csv_string, temp_json_file_path)

        # Read the result from the temporary JSON file
        with open(temp_json_file_path, 'r', encoding='utf-8') as json_file:
            result = json.load(json_file)

        expected_json = [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 25.5}
        ]

        # Assert the result matches the expected JSON output
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()
