import json
import csv

# Open JSON file and CSV file
with open('Jobs Data.json', 'r', encoding='utf-8') as json_file, open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    # Get all unique field names from the JSON objects
    fieldnames = set()
    for line in json_file:
        data = json.loads(line)
        fieldnames.update(data.keys())

    writer = csv.DictWriter(csv_file, fieldnames=list(fieldnames))
    writer.writeheader()  # Write CSV header

    # Reset file pointer to the beginning of the file
    json_file.seek(0)

    # Read JSON file line by line
    for line in json_file:
        data = json.loads(line)  # Load JSON object from each line
        writer.writerow(data)  # Write JSON object to CSV file

print("CSV file created successfully!")
