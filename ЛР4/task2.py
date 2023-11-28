# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def convert_csv_to_json(input_filename, output_filename):
    with open(input_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader)

        data = []

        for row in csv_reader:
            row_dict = {header: value for header, value in zip(headers, row)}
            data.append(row_dict)

    json_data = json.dumps(data, indent=4)

    with open(output_filename, 'w') as json_file:
        json_file.write(json_data)

def task() -> None:
    convert_csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
