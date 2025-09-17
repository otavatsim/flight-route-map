import csv
import json

# Replace with the path to your downloaded CSV file
csv_file_path = 'airports.csv'
json_file_path = 'airports.json'

# Initialize an empty list to hold airport data
airports = []

# Open the CSV file for reading
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract relevant fields and append to the list
        airports.append({
            "code": row['IATA'] if row['IATA'] else row['ICAO'],
            "name": row['Name'],
            "lat": float(row['Latitude']),
            "lon": float(row['Longitude'])
        })

# Write the list to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(airports, jsonfile, indent=2)

print(f"Conversion complete. JSON saved to {json_file_path}")
