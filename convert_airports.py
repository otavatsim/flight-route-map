import csv
import json

input_file = "airports.csv"       # downloaded file
output_file = "airports.json"     # the file Mapbox will use

airports = []
with open(input_file, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # prefer IATA code, fall back to ICAO if needed
        code = row["iata_code"] or row["ident"]
        name = row["name"]
        lat = row["latitude_deg"]
        lon = row["longitude_deg"]

        if code and lat and lon:
            airports.append({
                "code": code.strip(),
                "name": name.strip(),
                "lat": float(lat),
                "lon": float(lon)
            })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(airports, f, indent=2)

print(f"Saved {len(airports)} airports to {output_file}")
