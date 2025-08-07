#!/usr/bin/env python3
import os
import json
import csv

# Directory containing the JSON files
DATA_DIR = "pokemon_data"
# Output CSV file
CSV_FILE = "pokemon_report.csv"

total_height = 0
total_weight = 0
count = 0

# Open CSV file for writing
with open(CSV_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Height (m)", "Weight (kg)"])

    # Loop through each JSON file
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(DATA_DIR, filename)) as f:
                data = json.load(f)
                name = data["name"]
                height_m = round(data["height"] / 10, 2)
                weight_kg = round(data["weight"] / 10, 2)

                writer.writerow([name, height_m, weight_kg])

                total_height += height_m
                total_weight += weight_kg
                count += 1

# Calculate averages
avg_height = round(total_height / count, 2)
avg_weight = round(total_weight / count, 2)

# Print final output
print(f"CSV Report generated at: {CSV_FILE}\n")
with open(CSV_FILE) as f:
    print(f.read())
print(f"Average Height: {avg_height} m")
print(f"Average Weight: {avg_weight} kg")
