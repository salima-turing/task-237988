import csv
import json
import pandas as pd

# Dummy data: CSV file with metadata
dummy_csv_data = """
Title,Author,Description,Keywords,Publish Date
"The Great Gatsby","F. Scott Fitzgerald","A novel set in the Jazz Age","gatsby,novel,jazz,1920s",1925-04-10
"To Kill a Mockingbird","Harper Lee","A novel exploring themes of racism and injustice","mockingbird,novel,racism,injustice",1960-07-11
"""

# Example 1: Extracting and transforming metadata using CSV

# Write the dummy data to a temporary CSV file
with open('dummy_metadata.csv', 'w', newline='') as file:
    file.write(dummy_csv_data)

# Read the CSV file
with open('dummy_metadata.csv', 'r') as file:
    reader = csv.DictReader(file)
    metadata_list = []
    for row in reader:
        # Transform the data (e.g., convert date to ISO format)
        row['Publish Date'] = pd.to_datetime(row['Publish Date']).isoformat()
        metadata_list.append(row)

# Print the transformed metadata
print(json.dumps(metadata_list, indent=2))
